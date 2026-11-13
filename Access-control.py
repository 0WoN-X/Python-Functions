def check_access(role):
    if role == "admin":
        return "Full access"
    elif role == "user":
        return "Limited access"
    else:
        return "Access denied"

print(check_access("admin"))