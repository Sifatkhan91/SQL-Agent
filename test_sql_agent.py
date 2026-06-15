from app.agents.sql_agent import (
    run_sql_agent
)

response = run_sql_agent(
    "Show all customers"
)

print("\n")

print(
    response["answer"]
)