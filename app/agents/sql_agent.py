from app.agents.sql_generator import (
    generate_sql
)

from app.agents.result_explainer import (
    explain_result
)

from app.agents.sql_fixer import (
    fix_sql
)

from app.database.sql_executor import (
    execute_sql
)

from app.memory.memory_manager import (

    save_message

)


def run_sql_agent(
    question,
    session_id="default"
):

    save_message(

        session_id,

        "user",

        question

    )

    sql_query = generate_sql(

        question,

        session_id

    )

    print(
        "\nGenerated SQL:\n"
    )

    print(sql_query)

    result = execute_sql(
        sql_query
    )

    if not result["success"]:

        print(
            "\nFixing SQL...\n"
        )

        fixed_sql = fix_sql(

            question,

            sql_query,

            result["error"]

        )

        print(
            "\nFixed SQL:\n"
        )

        print(
            fixed_sql
        )

        result = execute_sql(
            fixed_sql
        )

        sql_query = fixed_sql

    if result["success"]:

        explanation = explain_result(

            question,

            sql_query,

            result["data"]

        )

        save_message(

            session_id,

            "assistant",

            explanation

        )

        return {

            "sql": sql_query,

            "result": result,

            "answer": explanation

        }

    return {

        "sql": sql_query,

        "result": result

    }