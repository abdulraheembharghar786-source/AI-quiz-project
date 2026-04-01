# AI-quiz-project
AI quiz application project

# Live demo link :- https://youtu.be/O5xr3qa3i1o?si=en986WYuykJnOV5x

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


   ----------------------------------------------------------------------------

   # Quiz Application with Document-Based Question Generation and LLM Evaluation

## 📌 Project Overview

This project is an AI-powered quiz system that automatically generates quiz questions from uploaded documents and evaluates user answers using a Large Language Model (LLM).

The system provides intelligent feedback, scoring, and performance summaries.

It is built entirely using open-source technologies and runs locally without requiring internet access.

---

## 🎯 Problem Understanding

Traditional quiz systems require manual question creation and basic answer checking methods. These systems are time-consuming and cannot evaluate descriptive answers intelligently.

Educators and trainers need automated systems that can generate questions from study materials and provide meaningful feedback to learners.

### Problem Statement

How to automatically generate quiz questions from documents and evaluate user answers intelligently using Artificial Intelligence.

### Key Issues Identified

- Manual question preparation takes time
- No intelligent evaluation of descriptive answers
- Limited feedback for students
- Lack of automated assessment systems
- Dependence on human graders

### Objective of the Project

- Automatically generate quiz questions from documents
- Evaluate answers using AI
- Provide feedback and scores
- Improve learning and assessment efficiency
- Reduce manual workload

---

## 🔍 Research Findings

Research was conducted on:

- AI-based question generation
- Automated grading systems
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Online quiz platforms

### Observations

Most systems generate questions but do not evaluate answers intelligently.

### Technologies Researched

- Natural Language Processing
- Machine Learning
- Large Language Models
- Document processing libraries
- Web application frameworks

### Research Conclusion

Large Language Models can understand text, generate questions, and evaluate answers more effectively than traditional rule-based systems.

---

## 🛠 Approach Taken

The project was developed using a modular architecture with separate components for:

- Document processing
- Question generation
- Answer evaluation
- User interface
- Result visualization

### System Workflow

User uploads document  
↓  
Text extraction  
↓  
Question generation  
↓  
User answers questions  
↓  
Answer evaluation  
↓  
Feedback and result summary  

### Implementation Steps

1. Build frontend interface
2. Implement backend API
3. Integrate AI model
4. Process documents
5. Generate questions
6. Evaluate answers
7. Display results

---

## ⚙️ Technologies Used

### Backend
- FastAPI

### Frontend
- Streamlit

### Server
- Uvicorn

### AI Model
- Mistral (LLM)

### AI Runtime
- Ollama

### Document Processing
- PyPDF2

### Programming Language
- Python

---

## 🔄 Alternatives Tried

### Alternative 1 — Rule-Based Question Generation

Method:

Generate questions using predefined rules.

Example:

If sentence contains "is", generate question "What is..."

Problems:

- Limited flexibility
- Poor accuracy
- Not scalable

Result:

Rejected

---

### Alternative 2 — Keyword Matching Evaluation

Method:

Check if user answer contains keywords.

Problems:

- Cannot understand meaning
- Incorrect scoring
- No feedback

Result:

Rejected

---

### Alternative 3 — Cloud-Based AI APIs

Method:

Use external AI APIs.

Problems:

- Internet required
- API cost
- Privacy concerns

Result:

Not selected

---

### Final Approach Selected

Local Large Language Model using Ollama.

Reasons:

- Works offline
- Free
- Accurate
- Customizable

---

## 🚧 Challenges Faced

### Challenge 1 — Model Setup

Problem:

Installing and running the AI model locally.

Solution:

Installed Ollama and downloaded the Mistral model.

---

### Challenge 2 — Multiple Python Versions

Problem:

Modules installed in wrong Python version.

Error:

ModuleNotFoundError

Solution:

Created virtual environment.

---

### Challenge 3 — Backend Connection Error

Problem:

Frontend could not connect to backend.

Error:

Connection refused

Solution:

Started backend server before frontend.

---

### Challenge 4 — UI Design

Problem:

Basic interface was not user-friendly.

Solution:

Developed website-level user interface.

---

## 📚 Learnings

### Technical Learnings

- Building web applications using Python
- Integrating AI models
- Processing documents
- Designing APIs
- Debugging system errors
- Building user interfaces

### AI and Machine Learning Learnings

- Understanding Large Language Models
- Natural Language Processing concepts
- Text generation techniques
- Answer evaluation using AI

### Development Learnings

- System design
- Error handling
- Testing and debugging
- Version management
- Problem solving

---

## ❌ Failed Attempts / Iterations

### Failed Attempt 1 — Basic Question Generator

Initial design:

Generate questions using simple text rules.

Problem:

Questions were repetitive and inaccurate.

Improvement:

Switched to AI model-based generation.

---

### Failed Attempt 2 — Manual Scoring System

Initial design:

Score answers using keyword matching.

Problem:

Incorrect scoring and no explanation.

Improvement:

Implemented LLM-based evaluation.

---

## 📈 Improvements Over Time

### Version 1 — Basic System

Features:

- Upload document
- Generate questions

Limitations:

- No evaluation
- No feedback

---

### Version 2 — Improved System

Features:

- Answer evaluation added
- Score calculation added

---

### Version 3 — Final System

Features:

- Website-level UI
- Feedback generation
- Result dashboard
- Error handling
- Local AI model

---

## 🏆 Final Improvement Summary

Basic system → Intelligent AI system

---

## 🚀 Future Enhancements

- Add voice input support
- Add multi-language support
- Add adaptive difficulty
- Deploy to cloud
- Add user authentication
- Add analytics dashboard

---

## 📄 License

This project is open-source and available under the MIT License.
