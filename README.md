# Doc Analyzer

An AI-powered resume parser built with Python, Groq and Pydantic. It extracts text from documents, uses an LLM to identify candidate information, validates the extracted data, and saves the result as structured JSON.

## Features

- **Multi-format support:** Read PDF, DOCX and TXT files.
- **Text extraction:** Extract text from supported document formats.
- **AI-powered extraction:** Use Groq LLMs to identify candidate details from resumes.
- **Structured data:** Organize candidate information into a consistent schema.
- **Data validation:** Validate extracted information using Pydantic models.
- **JSON export:** Save candidate profiles as JSON files.
- **Error handling:** Handle unsupported formats, missing files, corrupted documents and API errors.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | LLM-powered information extraction |
| Pydantic | Data validation and structured output |
| pypdf | PDF text extraction |
| python-docx | DOCX text extraction |
| python-dotenv | Environment variable management |
| uv | Dependency and project management |

## How It Works

```text
Resume (PDF / DOCX / TXT)
          |
          v
    File Handler
          |
          v
     Text Extraction
          |
          v
       Groq LLM
          |
          v
 Candidate Information
       Extraction
          |
          v
   Pydantic Validation
          |
          v
      JSON Output
```

## Project Structure

```text
doc_analyzer/
│
├── data/
│   └── resumes/             # Input resumes (local)
│
├── output/                  # Generated output (local)
│
├── ai_extractor.py          # Groq AI integration
├── file_handler.py          # PDF, DOCX and TXT processing
├── models.py                # Pydantic data models
├── profile_cleaner.py       # Profile cleaning and JSON handling
├── main.py                  # Application entry point
│
├── .env                     # API credentials (not committed)
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/1930Saurabh/doc-analyzer.git
cd doc-analyzer
```

### 2. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if you haven't already, then run:

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Never commit your `.env` file or expose your API key publicly.

## Usage

Run the application:

```bash
uv run main.py
```

When prompted, enter the path to your resume:

```text
Enter resume file path: data/resumes/resume.pdf
```

The application will extract the document text, send it to the Groq model, validate the candidate information and save the result.

## Output

The generated candidate profile is saved in:

```text
output/cleaned_profile.json
```

Example output structure:

```json
{
    "name": "Candidate Name",
    "email": "candidate@example.com",
    "phone": "1234567890",
    "summary": "Candidate professional summary",
    "experience": [],
    "projects": [],
    "education": [],
    "skills": [],
    "certificates": [],
    "links": {}
}
```

The actual output contains the information extracted from the supplied resume.

## Current Limitations

- Currently focused on resume and candidate information extraction.
- Requires a valid Groq API key.
- Scanned PDFs may require OCR support, which is not currently implemented.
- No graphical frontend yet; the application runs through the terminal.

## Future Improvements

- Web-based document upload interface.
- General-purpose document analysis.
- Document summarization and key information extraction.
- Multiple document processing.
- Document question-answering using RAG.
- Downloadable structured reports.

## Author

**Saurabh Sinha**

GitHub: [@1930Saurabh](https://github.com/1930Saurabh)

---

*Built as a hands-on AI engineering project to explore Python, LLM integration, structured extraction and data validation.*
