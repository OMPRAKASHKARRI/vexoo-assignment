def route_query(query):
    query = query.lower()

    if any(word in query for word in ["calculate", "sum", "math"]):
        return "math"

    elif any(word in query for word in ["law", "legal"]):
        return "legal"

    else:
        return "general"