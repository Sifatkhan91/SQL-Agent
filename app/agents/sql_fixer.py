from app.services.openai_service import (
    ask_openai
)

from app.database.schema_reader import (
    get_schema
)


def fix_sql(
    question,
    bad_sql,
    error
):

    schema = get_schema()

    prompt = f"""
You are a PostgreSQL expert.

Database Schema:

{schema}

User Question:

{question}

Generated SQL:

{bad_sql}

Database Error:

{error}

Fix the SQL.

Rules:

- Return ONLY SQL
- No markdown
- No explanation
"""

    fixed_sql = ask_openai(
        prompt
    )

    return (
        fixed_sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )