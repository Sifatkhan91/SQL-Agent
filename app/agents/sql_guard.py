def is_safe_sql(sql_query):

    sql_upper = sql_query.upper()

    blocked_keywords = [

        "DROP",

        "DELETE",

        "TRUNCATE",

        "UPDATE",

        "INSERT",

        "ALTER",

        "CREATE"

    ]

    for keyword in blocked_keywords:

        if keyword in sql_upper:

            return False

    return True