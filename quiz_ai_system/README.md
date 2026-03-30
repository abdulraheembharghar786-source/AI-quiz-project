
# Intelligent Quiz Application with Document-Based Question Generation and LLM Evaluation

## Features
- Upload document (PDF/DOCX/TXT)
- Topic-based question generation using LLM
- Answer evaluation using rubric scoring
- Feedback generation
- Result summary

## Run Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Start backend:
   uvicorn backend.main:app --reload

3. Run frontend:
   streamlit run frontend/app.py
