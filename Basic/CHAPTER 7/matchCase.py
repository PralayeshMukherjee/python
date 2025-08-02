def http_status(status) -> str:
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "server error"
        case _:
            return "unknown"
print(http_status(500));