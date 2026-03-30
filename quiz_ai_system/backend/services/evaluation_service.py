
import ollama

def evaluate_answer(question, correct_answer, user_answer):

    prompt = f"""
    Evaluate the student's answer using the rubric:

    Accuracy — 4 points
    Completeness — 3 points
    Clarity — 2 points
    Relevance — 1 point

    Question:
    {question}

    Correct Answer:
    {correct_answer}

    User Answer:
    {user_answer}

    Return:
    Score:
    Feedback:
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
