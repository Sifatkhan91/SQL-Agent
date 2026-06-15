from app.database.sql_executor import (
    execute_sql
)

result = execute_sql(
    """
    SELECT *
    FROM customers
    """
)

print(result)