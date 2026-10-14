
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_questions():
    return [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?",
        "What are your weaknesses?",
        "Where do you see yourself in 5 years?"
    ]


def evaluate(answer):
    prompt = f"""
You are an experienced HR interviewer.

Evaluate the following interview answer.

Give:
- Score out of 10
- Strengths
- Weaknesses
- Suggestions

Answer:
{answer}
"""
    response = model.generate_content(prompt)
    return response.text
