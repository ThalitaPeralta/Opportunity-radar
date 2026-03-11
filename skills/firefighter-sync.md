You are running the Firefighter Ticket Sync skill.

## What this skill does
Fetches all open Firefighter-type tickets from Jira (project: LH, instance: laserhub.atlassian.net)
and appends any new ones to a Google Sheet. On the very first run it creates the spreadsheet automatically.

## Columns exported
| Column | Source |
|---|---|
| Ticket | Jira issue key (e.g. LH-123) |
| Link | Direct URL to the Jira ticket |
| Summary | Ticket title |
| Description | Full ticket description (plain text) |
| Reporter | Who opened the ticket |
| Created Date | Date the ticket was opened (YYYY-MM-DD) |
| Status | Current status (e.g. Open, In Progress, Done) |
| Priority | Ticket priority |

## Steps to run

1. Make sure credentials are set up:
   - Copy `.env.example` → `.env` and fill in `JIRA_EMAIL`, `JIRA_API_TOKEN`, `GOOGLE_CREDENTIALS_FILE`
   - Place your Google service account JSON at the path specified in `GOOGLE_CREDENTIALS_FILE`

2. Install dependencies (first time only):
   ```
   pip install -r scripts/requirements.txt
   ```

3. Run the sync:
   ```
   python scripts/firefighter_sync.py
   ```

4. The script will print the Google Sheet URL on every run.
   The sheet ID is saved in `scripts/firefighter_config.json` so subsequent runs append to the same sheet.

## To schedule daily (cron / Task Scheduler)
**Mac/Linux cron** — runs every day at 8 AM:
```
0 8 * * * cd /path/to/Opportunity-radar && python scripts/firefighter_sync.py >> logs/firefighter.log 2>&1
```

**Windows Task Scheduler:**
- Action: `python`
- Arguments: `C:\path\to\Opportunity-radar\scripts\firefighter_sync.py`
- Trigger: Daily at preferred time

## Google Service Account setup (one-time)
1. Go to https://console.cloud.google.com/
2. Create a project (or use an existing one)
3. Enable **Google Sheets API** and **Google Drive API**
4. Create a **Service Account** → generate a JSON key → download it
5. Place the JSON file in this repo root and set `GOOGLE_CREDENTIALS_FILE=credentials.json` in `.env`
6. On the first run, the script prints the new spreadsheet URL — open it and **share it with your team**
