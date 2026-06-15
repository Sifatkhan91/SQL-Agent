from typing import TypedDict


class SQLAgentState(
    TypedDict,
    total=False
):

    question: str

    session_id: str

    intent: str

    sql_query: str

    result: dict

    error: str

    answer: str