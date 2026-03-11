"""
Firefighter Ticket Sync
-----------------------
Fetches all Firefighter issue-type tickets from Jira (project: LH)
and appends new ones daily to a Google Sheet.

First run: creates the spreadsheet automatically.
Subsequent runs: appends only tickets not yet in the sheet.

Required env vars (see .env.example):
  JIRA_EMAIL, JIRA_API_TOKEN, GOOGLE_CREDENTIALS_FILE
"""

import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
JIRA_BASE_URL    = "https://laserhub.atlassian.net"
JIRA_EMAIL       = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN   = os.environ["JIRA_API_TOKEN"]
JQL              = 'project = LH AND issuetype = Firefighter ORDER BY created DESC'

GOOGLE_CREDS     = os.environ.get("GOOGLE_CREDENTIALS_FILE", "credentials.json")
SHEET_TITLE      = "Firefighter Tickets - Laserhub"
SHEET_TAB        = "Firefighter Tickets"
CONFIG_FILE      = Path(__file__).parent / "firefighter_config.json"
SCOPES           = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
HEADERS = ["Ticket", "Link", "Summary", "Description", "Reporter", "Created Date", "Status", "Priority"]


# ---------------------------------------------------------------------------
# Jira helpers
# ---------------------------------------------------------------------------
def fetch_jira_tickets() -> list[dict]:
    url    = f"{JIRA_BASE_URL}/rest/api/3/search"
    auth   = (JIRA_EMAIL, JIRA_API_TOKEN)
    params = {
        "jql":        JQL,
        "fields":     "summary,description,reporter,created,status,priority",
        "maxResults": 200,
    }
    response = requests.get(url, params=params, auth=auth)
    response.raise_for_status()
    return response.json().get("issues", [])


def parse_adf_description(description) -> str:
    """Convert Atlassian Document Format (ADF) to plain text."""
    if not description:
        return ""
    if isinstance(description, str):
        return description.strip()
    texts: list[str] = []

    def _walk(node: dict):
        if node.get("type") == "text":
            texts.append(node.get("text", ""))
        for child in node.get("content", []):
            _walk(child)

    _walk(description)
    return " ".join(texts).strip()


def format_date(iso_str: str) -> str:
    """Return YYYY-MM-DD from an ISO 8601 string."""
    if not iso_str:
        return ""
    try:
        return iso_str[:10]
    except Exception:
        return iso_str


# ---------------------------------------------------------------------------
# Google Sheets helpers
# ---------------------------------------------------------------------------
def get_sheets_service():
    creds = Credentials.from_service_account_file(GOOGLE_CREDS, scopes=SCOPES)
    return build("sheets", "v4", credentials=creds)


def load_config() -> dict:
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


def save_config(data: dict):
    CONFIG_FILE.write_text(json.dumps(data, indent=2))


def get_or_create_spreadsheet(service) -> str:
    config   = load_config()
    sheet_id = config.get("spreadsheet_id")

    if sheet_id:
        try:
            service.spreadsheets().get(spreadsheetId=sheet_id).execute()
            return sheet_id
        except HttpError:
            print("Stored spreadsheet not found — creating a new one.")

    # Build spreadsheet with header row
    header_values = [{"userEnteredValue": {"stringValue": h}} for h in HEADERS]
    body = {
        "properties": {"title": SHEET_TITLE},
        "sheets": [{
            "properties": {"title": SHEET_TAB},
            "data": [{"startRow": 0, "startColumn": 0,
                      "rowData": [{"values": header_values}]}],
        }],
    }
    result   = service.spreadsheets().create(body=body).execute()
    sheet_id = result["spreadsheetId"]
    config["spreadsheet_id"] = sheet_id
    save_config(config)

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
    print(f"Created new spreadsheet: {url}")
    return sheet_id


def get_existing_ticket_ids(service, sheet_id: str) -> set[str]:
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f"{SHEET_TAB}!A:A",
    ).execute()
    rows = result.get("values", [])
    return {row[0] for row in rows[1:] if row}  # skip header


def append_rows(service, sheet_id: str, rows: list[list]):
    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=f"{SHEET_TAB}!A:{chr(ord('A') + len(HEADERS) - 1)}",
        valueInputOption="USER_ENTERED",
        body={"values": rows},
    ).execute()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}] Starting Firefighter sync...")

    # 1. Fetch tickets from Jira
    issues = fetch_jira_tickets()
    print(f"  Jira returned {len(issues)} Firefighter ticket(s)")

    # 2. Connect to Google Sheets
    service  = get_sheets_service()
    sheet_id = get_or_create_spreadsheet(service)

    # 3. Determine which tickets are already logged
    existing_ids = get_existing_ticket_ids(service, sheet_id)
    print(f"  Sheet already contains {len(existing_ids)} ticket(s)")

    # 4. Build rows for new tickets only
    new_rows: list[list] = []
    for issue in issues:
        key = issue["key"]
        if key in existing_ids:
            continue

        fields = issue.get("fields", {})
        row = [
            key,
            f"{JIRA_BASE_URL}/browse/{key}",
            fields.get("summary", ""),
            parse_adf_description(fields.get("description")),
            (fields.get("reporter") or {}).get("displayName", ""),
            format_date(fields.get("created", "")),
            (fields.get("status") or {}).get("name", ""),
            (fields.get("priority") or {}).get("name", ""),
        ]
        new_rows.append(row)

    # 5. Append and report
    if new_rows:
        append_rows(service, sheet_id, new_rows)
        print(f"  Appended {len(new_rows)} new ticket(s)")
    else:
        print("  No new tickets to append")

    print(f"  Sheet: https://docs.google.com/spreadsheets/d/{sheet_id}")
    print("Done.")


if __name__ == "__main__":
    main()
