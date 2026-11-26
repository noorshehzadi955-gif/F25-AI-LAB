# Lab 6 - Task 1: Tokenization and a FAQ Chatbot

## Scope
This folder completes Task 1 (Beginner) only. Tasks 2 and 3 are not included.

## Files
- `task1_tokens.py` - compares whitespace and Unicode word-like regex tokens for six required inputs.
- `lab6_search.py` - TF-IDF retrieval helper.
- `guided_chatbot.py` - interactive FAQ chatbot with five FAQs.
- `task1_chatbot_check.py` - tests exact answer, suggestion, empty input and unsupported input.
- `requirements.txt` - required package.
- `Lab6_Report.docx` - explanation and actual outputs.
- `outputs/` - captured terminal outputs and chatbot transcript.

## Setup
Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\\Scripts\\Activate.ps1
```

Install:
```bash
python -m pip install -r requirements.txt
```

## Run
```bash
python task1_tokens.py
python guided_chatbot.py
python task1_chatbot_check.py
```

## Optional model tokenizer
To enable the model subword comparison, install `sentence-transformers`. The first run may download the model:
```bash
python -m pip install sentence-transformers
```
If it is unavailable, the required whitespace and regex comparison still runs.

## Chatbot behavior
- Exact stored question: returns answer and source.
- Nonexact question: displays possible FAQ suggestions for confirmation.
- Empty input: asks the user to enter a question.
- Unsupported query: displays a help-desk fallback.

The FAQ records are synthetic teaching examples. Their source filenames are illustrative labels, not verified university policy documents.
