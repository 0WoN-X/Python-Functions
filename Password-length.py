def check_password(password):
    if len(password) >= 8:
        return "Password length is acceptable"
    else:
        return "Password is too short"

print(check_password("hello12345"))