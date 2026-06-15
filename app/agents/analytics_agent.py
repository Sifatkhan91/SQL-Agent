from app.database.sql_executor import (
    execute_sql
)

from app.services.openai_service import (
    ask_openai
)


def run_analytics(question):

    analytics_queries = {

        "total revenue":
        """
        SELECT
        SUM(amount) AS total_revenue
        FROM orders
        """,

        "top customers":
        """
        SELECT
            c.customer_name,
            SUM(o.amount) AS total_spent
        FROM customers c
        JOIN orders o
        ON c.customer_id = o.customer_id
        GROUP BY c.customer_name
        ORDER BY total_spent DESC
        LIMIT 5
        """,

        "customer distribution":
        """
        SELECT
            city,
            COUNT(*) AS total_customers
        FROM customers
        GROUP BY city
        ORDER BY total_customers DESC
        """
    }

    question_lower = question.lower()

    selected_sql = None

    for key in analytics_queries:

        if key in question_lower:

            selected_sql = analytics_queries[key]

            break

    if not selected_sql:

        return None

    result = execute_sql(
        selected_sql
    )

    if not result["success"]:

        return result

    prompt = f"""
User Question:

{question}

Analytics Data:

{result['data']}

Provide a business-friendly summary.
"""

    summary = ask_openai(
        prompt
    )

    return {

        "answer": summary,

        "data": result["data"]

    }