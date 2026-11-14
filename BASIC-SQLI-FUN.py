def detect_sql_injection(user_input):

    suspicious_words = [
        "SELECT",
        "DROP",
        "DELETE",
        "INSERT",
        "UPDATE",
        "OR 1=1",
        "UNION",
        "--"
    ]

    for word in suspicious_words:
        if word in user_input.upper():
            return "Warning: Suspicious SQL input detected!"

    return "Input looks normal"

