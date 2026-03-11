Read the file `instructions-to-opportunity-radar-automation-plan` from the repo root.

Summarize it as a clear, concise email addressed to a product team. Cover:
- The goal
- The inputs
- The business logic
- The expected outcomes

Keep it under 300 words. Use bullet points where helpful. Write in plain English, no jargon.

Then save the summary to `output/latest-summary.md` (create the file if it doesn't exist, overwrite if it does).

After saving, run this command to send it:
```
python scripts/send_email.py
```

Confirm to the user when the email has been sent and show them the path to the saved summary.
