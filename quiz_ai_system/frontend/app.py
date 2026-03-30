
import streamlit as st
import requests

st.title("AI Quiz Application")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    if st.button("Upload"):
        files = {"file": uploaded_file}
        requests.post("http://localhost:8000/upload", files=files)
        st.success("Document uploaded")

if st.button("Generate Questions"):
    response = requests.get("http://localhost:8000/generate-questions")
    st.write(response.json())

question = st.text_input("Question")
correct_answer = st.text_input("Correct Answer")
user_answer = st.text_input("Your Answer")

if st.button("Evaluate Answer"):
    response = requests.post(
        "http://localhost:8000/evaluate",
        params={
            "question": question,
            "correct_answer": correct_answer,
            "user_answer": user_answer
        }
    )
    st.write(response.json())
