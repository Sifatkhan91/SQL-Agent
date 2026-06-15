conversation_memory = {}


def save_message(
    session_id,
    role,
    content
):

    if session_id not in conversation_memory:

        conversation_memory[
            session_id
        ] = []

    conversation_memory[
        session_id
    ].append(

        {
            "role": role,
            "content": content
        }

    )


def get_history(
    session_id
):

    return conversation_memory.get(
        session_id,
        [])


def get_conversation_summary(
    session_id
):

    history = get_history(
        session_id
    )

    if not history:

        return (
            "No conversation history found."
        )

    summary = ""

    for item in history:

        summary += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    return summary