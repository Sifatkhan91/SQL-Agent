from app.agents.analytics_agent import (
    run_analytics
)

response = run_analytics(
    "Who are the top customers?"
)

print(
    response["answer"]
)