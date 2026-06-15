from langgraph.graph import (
    StateGraph,
    END
)

from app.agents.state import (
    SQLAgentState
)

from app.agents.nodes import (

    router_node,

    analytics_node,

    memory_node,

    generate_sql_node,

    execute_sql_node,

    fix_sql_node,

    explain_result_node,

    route_intent,

    route_after_execution

)


def build_graph():

    workflow = StateGraph(
        SQLAgentState
    )

    workflow.add_node(
        "router",
        router_node
    )

    workflow.add_node(
        "analytics",
        analytics_node
    )

    workflow.add_node(
        "memory",
        memory_node
    )

    workflow.add_node(
        "generate_sql",
        generate_sql_node
    )

    workflow.add_node(
        "execute_sql",
        execute_sql_node
    )

    workflow.add_node(
        "fix_sql",
        fix_sql_node
    )

    workflow.add_node(
        "explain",
        explain_result_node
    )

    workflow.set_entry_point(
        "router"
    )

    workflow.add_conditional_edges(

        "router",

        route_intent,

        {

            "sql":
            "generate_sql",

            "analytics":
            "analytics",

            "memory":
            "memory"

        }

    )

    workflow.add_edge(
        "analytics",
        END
    )

    workflow.add_edge(
        "memory",
        END
    )

    workflow.add_edge(
        "generate_sql",
        "execute_sql"
    )

    workflow.add_conditional_edges(

        "execute_sql",

        route_after_execution,

        {

            "fix":
            "fix_sql",

            "explain":
            "explain",

            "end":
            END

        }

    )

    workflow.add_edge(
        "fix_sql",
        "execute_sql"
    )

    workflow.add_edge(
        "explain",
        END
    )

    return workflow.compile()