#  AI Meeting Summary + CRM Note Generator

This project is an AI-powered web app that generates meeting summaries and CRM-style notes from **text input**. Paste your meeting transcript or notes, and the system will extract a clear summary, key decisions, and follow-ups.

---

## Features

-  Accepts **direct text input** (no audio required)
-  AI-generated meeting summaries using GPT models
-  Actionable CRM notes: decisions, follow-ups, next steps
-  Clean and minimal web interface with Flask backend
-  Built for sales teams, consultants, and managers

---

##  Project Overview

Instead of uploading audio, users paste meeting transcripts or manually enter meeting notes. The system uses OpenAI's GPT model to produce:

- A short meeting summary
- Key action points and decisions
- Follow-up tasks in CRM format

### Tech Stack

- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Python (Flask)
- **AI Model**: OpenAI GPT (text analysis and summarization)

---

##  Folder Structure

```bash
ai-meeting-summary/
├── app.py                 # Flask backend
├── static/
│   └── styles.css         # Custom styling
├── templates/
│   ├── index.html         # Home page with input form
│   └── result.html        # Displays summary and CRM notes
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
How It Works
- User enters a raw transcript or notes
- GPT model processes the text

Outputs:
- Concise meeting summary
- CRM-style follow-ups & actions

Future Plans
-PDF/Email export

-Speech-to-text integration (optional)

-User login and history tracking

-Integration with Notion, Salesforce, etc.

Contributing
Pull requests are welcome! Open an issue first to propose a change or feature.

📄 License
This project is licensed under the MIT License.
