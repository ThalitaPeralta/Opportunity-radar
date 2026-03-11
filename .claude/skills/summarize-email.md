You are running the Summarize & Email skill.

## What this skill does
Reads the file `instructions-to-opportunity-radar-automation-plan`, summarizes it using
the Claude API, and sends the summary by email to thaperalta@gmail.com via SendGrid.

## How to run manually (in Cursor terminal)
```
python scripts/summarize_email.py
```

## How it runs automatically (GitHub Actions)
Trigger it manually from the GitHub Actions tab:
1. Go to your repo on GitHub
2. Click **Actions** → **Summarize & Email**
3. Click **Run workflow**

The workflow runs twice automatically:
- **Run 1**: immediately on trigger
- **Run 2**: 5 minutes after Run 1 completes

## Required secrets (set in GitHub repo settings)
| Secret | Where to get it |
|---|---|
| `ANTHROPIC_API_KEY` | console.anthropic.com → API Keys |
| `SENDGRID_API_KEY` | app.sendgrid.com → Settings → API Keys |
| `SENDGRID_FROM_EMAIL` | A verified sender email in your SendGrid account |

## Required env vars (for local runs)
Copy `.env.example` → `.env` and fill in the three values above.
