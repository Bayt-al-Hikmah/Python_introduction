import re
password = input("Enter password:")
def check_valid(password: str) -> bool :
    return bool(re.match("^[a-zA-Z]([a-zA-Z]|[^a-zA-Z0-9][0-9])([a-zA-Z]|[^a-zA-Z0-9][0-9])*",password)) and len(password) >=10
print(check_valid(password))