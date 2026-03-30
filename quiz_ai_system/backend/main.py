
from fastapi import FastAPI, UploadFile
from backend.services.document_service import load_document
from backend.services.question_service import generate_questions
from backend.services.evaluation_service import evaluate_answer

app = FastAPI()

document_text = ""
questions_store = []

@app.post("/upload")
async def upload_document(file: UploadFile):
    global document_text
    document_text = load_document(file.file)
    return {"message": "Document uploaded successfully"}

@app.get("/generate-questions")
def get_questions():
    global questions_store
    questions_store = generate_questions(document_text)
    return {"questions": questions_store}

@app.post("/evaluate")
def evaluate(question: str, correct_answer: str, user_answer: str):
    result = evaluate_answer(question, correct_answer, user_answer)
    return {"result": result}
