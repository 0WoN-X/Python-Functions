def login(username, password):
    correct_username = "admin"
    correct_password = "12345"

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        if username == correct_username and password == correct_password:
            return "Login successful!"

        attempts += 1
        print("Wrong credentials!")
        print("Attempts remaining:", max_attempts - attempts)

        if attempts == max_attempts:
            return "Account temporarily locked!"

    return "Login failed"


print(login("admin", "wrong"))