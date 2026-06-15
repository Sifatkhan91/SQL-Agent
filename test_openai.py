from app.services.openai_service import (
    ask_openai
)

response = ask_openai(
    "Say hello"
)

print(response)