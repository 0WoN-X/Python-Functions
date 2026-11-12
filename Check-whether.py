def login(username, password):
    if username == "admin" and password == "12345":
        return "Login successful"
    else:
        return "Access denied"

print(login("admin", "12345"))