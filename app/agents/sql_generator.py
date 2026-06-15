from app.memory.memory_manager import (
    get_history
)



from app.services.openai_service import (
    ask_openai
)

from app.database.schema_reader import (
    get_schema
)


def generate_sql(
    question,
    session_id="default"
):

    schema = get_schema()

    history = get_history(
        session_id
    )

    history_text = ""

    for item in history:

        history_text += (

            f"{item['role']}: "
            f"{item['content']}\n"

        )

    prompt = f"""
You are a PostgreSQL expert.

Database Schema:

{schema}

Conversation History:

{history_text}

Current Question:

{question}

Rules:

- Return ONLY SQL
- No markdown
- No explanation
"""

    sql = ask_openai(
        prompt
    )

    return (

        sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()

    )