# Lab 6 – Tokenization and FAQ Chatbot

## Objective
The objective of this task is to understand text tokenization techniques and create a simple FAQ chatbot using TF-IDF.

## Task 1: Tokenization
- Compared whitespace splitting and regex-based tokenization.
- Tested punctuation, contractions, email addresses, CS4944, empty text, and Urdu text.
- Printed token lists and token counts.
- Discussed tokenization differences and normalization risks.

## Task 2: FAQ Chatbot
- Created a simple FAQ chatbot using TF-IDF.
- Added frequently asked questions with answers and source labels.
- Tested exact answers, suggestions, empty input, and unsupported questions.
- Used confirmation for non-exact questions to avoid incorrect answers.

## Files
- `task1_tokens.py` – Tokenization comparison.
- `lab6_search.py` – TF-IDF retrieval system.
- `guided_chatbot.py` – FAQ chatbot.
- `task1_chatbot_check.py` – Chatbot testing.
- `requirements.txt` – Required Python package.
- `outputs/` – Program output files.
- `Lab6_Report.docx` – Lab report.

## How to Run

Install the required package:

```bash
pip install -r requirements.txt
```

Run tokenization:

```bash
python task1_tokens.py
```

Run the chatbot:

```bash
python guided_chatbot.py
```

Run chatbot tests:

```bash
python task1_chatbot_check.py
```

## Conclusion
This task demonstrates basic tokenization methods and a TF-IDF-based FAQ chatbot with source labels and suggestion handling.
