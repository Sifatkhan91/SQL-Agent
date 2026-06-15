from app.services.openai_service import (
    ask_openai
)


def explain_result(
    question,
    sql_query,
    result
):

    prompt = f"""
You are a business analyst.

User Question:

{question}

SQL Used:

{sql_query}

Database Result:

{result}

Explain the result in plain English.

Be concise and professional.
"""

    return ask_openai(
        prompt
    )