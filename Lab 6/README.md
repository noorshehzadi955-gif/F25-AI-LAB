## Description
A small text-retrieval pipeline that compares tokenization methods, three
chunking strategies, and TF-IDF vs sentence-embedding search, with FAQ and
document chatbots. All data is synthetic teaching data.

## Setup
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install numpy scikit-learn sentence-transformers

The first run downloads the model sentence-transformers/all-MiniLM-L6-v2.

## How to Run
- Task 1: python task1_tokens.py, then python guided_chatbot.py
- Task 2: python task2_chunks.py, then python guided_embeddings.py
- Task 3: python create_dataset.py, python task3_retrieval.py, python document_chatbot.py

## Main Files
- lab6_search.py - shared retriever (TF-IDF and embeddings)
- task1_tokens.py, task2_chunks.py, task3_retrieval.py - the three tasks
- document_chatbot.py - evidence chatbot
- corpus.json, queries.json, retrieval_log.csv - data and results
- Lab6_Report.docx - report and analysis

## Sources
Starter code adapted from the CAI601400 Lab 6 manual. Model:
sentence-transformers/all-MiniLM-L6-v2. Results and analysis are in the report.
