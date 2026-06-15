from app.agents.sql_generator import (
    generate_sql
)

from app.agents.sql_fixer import (
    fix_sql
)

from app.agents.result_explainer import (
    explain_result
)

from app.agents.router_agent import (
    classify_intent
)

from app.agents.analytics_agent import (
    run_analytics
)

from app.agents.sql_guard import (
    is_safe_sql
)

from app.memory.memory_manager import (
    get_conversation_summary
)

from app.database.sql_executor import (
    execute_sql
)


def router_node(state):

    intent = classify_intent(
        state["question"]
    )

    print(
        f"\nIntent: {intent}\n"
    )

    return {
        "intent": intent
    }


def analytics_node(state):

    result = run_analytics(
        state["question"]
    )

    return {
        "answer":
        result["answer"]
    }


def memory_node(state):

    history = get_conversation_summary(

        state.get(
            "session_id",
            "default"
        )

    )

    return {
        "answer":
        history
    }


def generate_sql_node(state):

    sql_query = generate_sql(

        state["question"],

        state.get(
            "session_id",
            "default"
        )

    )

    return {
        "sql_query":
        sql_query
    }


def execute_sql_node(state):

    if not is_safe_sql(
        state["sql_query"]
    ):

        return {

            "answer":
            "Blocked by SQL Safety Guard. Only SELECT queries are allowed.",

            "error":
            None
        }

    result = execute_sql(
        state["sql_query"]
    )

    if result["success"]:

        return {

            "result":
            result,

            "error":
            None

        }

    return {

        "error":
        result["error"]

    }


def fix_sql_node(state):

    fixed_sql = fix_sql(

        state["question"],

        state["sql_query"],

        state["error"]

    )

    return {

        "sql_query":
        fixed_sql,

        "error":
        None

    }


def explain_result_node(state):

    answer = explain_result(

        state["question"],

        state["sql_query"],

        state["result"]["data"]

    )

    return {

        "answer":
        answer

    }


def route_intent(state):

    return state["intent"]


def route_after_execution(state):

    if state.get(
        "answer"
    ):

        return "end"

    if state.get(
        "error"
    ):

        return "fix"

    return "explain"