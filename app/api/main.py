from fastapi import FastAPI

from app.api.models import (
    ChatRequest,
    ChatResponse
)

from app.agents.graph import (
    build_graph
)

app = FastAPI(
    title="SQL Agent API"
)

graph = build_graph()


@app.get("/")
def home():

    return {
        "message":
        "SQL Agent API Running"
    }


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    result = graph.invoke(

        {
            "question":
            request.question,

            "session_id":
            request.session_id
        }

    )

    return ChatResponse(

        answer=
        result["answer"]

    )