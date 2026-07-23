def http(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"

print(http(200))           