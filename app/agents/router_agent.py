from app.services.openai_service import (
    ask_openai
)


def classify_intent(question):

    prompt = f"""
Classify the user's intent.

Question:

{question}

Return ONLY one:

sql
analytics
memory
"""

    result = ask_openai(
        prompt
    )

    return (
        result
        .strip()
        .lower()
    )