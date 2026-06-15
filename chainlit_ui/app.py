import chainlit as cl

import requests

import uuid


API_URL = (
    "http://127.0.0.1:8001/chat"
)


@cl.on_chat_start
async def start():

    cl.user_session.set(

        "session_id",

        str(uuid.uuid4())

    )


@cl.on_message
async def main(message: cl.Message):

    session_id = cl.user_session.get(
        "session_id"
    )

    response = requests.post(

        API_URL,

        json={

            "question":
            message.content,

            "session_id":
            session_id

        }

    )

    answer = response.json()[
        "answer"
    ]

    await cl.Message(

        content=answer

    ).send()