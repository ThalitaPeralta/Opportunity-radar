"""
Summarize & Email
-----------------
Reads instructions-to-opportunity-radar-automation-plan,
summarizes it using the Claude API, and sends the summary
to thaperalta@gmail.com via SendGrid.

Required env vars (see .env.example):
  ANTHROPIC_API_KEY, SENDGRID_API_KEY, SENDGRID_FROM_EMAIL
"""

import os
from pathlib import Path
import anthropic
import sendgrid
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SOURCE_FILE       = Path(__file__).parent.parent / "instructions-to-opportunity-radar-automation-plan"
RECIPIENT_EMAIL   = "thaperalta@gmail.com"
SENDGRID_API_KEY  = os.environ["SENDGRID_API_KEY"]
FROM_EMAIL        = os.environ["SENDGRID_FROM_EMAIL"]


# ---------------------------------------------------------------------------
# Summarize with Claude
# ---------------------------------------------------------------------------
def summarize(content: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    "You are a product management assistant. "
                    "Read the following automation plan and write a concise email summary "
                    "covering: the goal, the inputs, the business logic, and the expected outcomes. "
                    "Keep it under 300 words, use bullet points where helpful, "
                    "and write it as if addressed to a product team.\n\n"
                    f"---\n{content}\n---"
                ),
            }
        ],
    )
    return message.content[0].text


# ---------------------------------------------------------------------------
# Send email via SendGrid
# ---------------------------------------------------------------------------
def send_email(summary: str):
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=RECIPIENT_EMAIL,
        subject="[Opportunity Radar] Automation Plan Summary",
        html_content=summary.replace("\n", "<br>"),
    )
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    response = sg.send(email)
    print(f"  Email sent — status: {response.status_code}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Reading source file...")
    content = SOURCE_FILE.read_text(encoding="utf-8")

    print("Summarizing with Claude...")
    summary = summarize(content)
    print(f"  Summary ({len(summary)} chars) generated")

    print(f"Sending email to {RECIPIENT_EMAIL}...")
    send_email(summary)

    print("Done.")


if __name__ == "__main__":
    main()
