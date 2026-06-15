from pydantic import BaseModel


class ChatRequest(BaseModel):

    question: str

    session_id: str = "default"


class ChatResponse(BaseModel):

    answer: str