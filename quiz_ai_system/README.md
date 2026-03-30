
# Intelligent Quiz Application with Document-Based Question Generation and LLM Evaluation

## Overview

This project is an open-source AI-based quiz system that accepts
documents, generates topic-based questions, evaluates answers using a
Large Language Model (LLM), and provides feedback and performance
summaries.

## Features

-   Document upload (PDF, DOCX, TXT)
-   Topic detection
-   Automatic question generation
-   Answer evaluation using rubric scoring
-   Feedback generation
-   Result summary dashboard

## Technologies Used

-   FastAPI
-   Streamlit
-   Uvicorn
-   Ollama
-   Mistral LLM
-   PyPDF2

## How to Run

1.  Install dependencies: pip install -r requirements.txt

2.  Start backend: uvicorn backend.main:app --reload


3. open another terminal and Start frontend: streamlit run frontend/app.py
