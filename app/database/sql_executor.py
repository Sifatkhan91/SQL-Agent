from sqlalchemy import text

from app.database.database import (
    engine
)


def execute_sql(sql_query):

    try:

        with engine.connect() as conn:

            result = conn.execute(
                text(sql_query)
            )

            rows = result.fetchall()

            columns = result.keys()

            data = []

            for row in rows:

                data.append(
                    dict(
                        zip(
                            columns,
                            row
                        )
                    )
                )

            return {
                "success": True,
                "data": data
            }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }