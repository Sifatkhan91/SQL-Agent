from app.agents.graph import (
    build_graph
)

graph = build_graph()

response = graph.invoke(

    {
        "question":
        "Show all customers"
    }

)

print("\n")

print(
    response["answer"]
)