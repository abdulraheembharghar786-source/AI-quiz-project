
import ollama

def generate_questions(text):
    prompt = f"""
    Generate 5 topic-based questions and answers from the following text:

    {text}

    Format:
    Q:
    Answer:
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
