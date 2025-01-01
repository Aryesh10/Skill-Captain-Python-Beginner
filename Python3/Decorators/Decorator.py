
def authorize(username):
    authorized_users = ["admin", "Aryesh", "skillcaptain"]

    def decorator(func):
        def wrapper(*args, **kwargs):
            if username in authorized_users:
                print(f"Access granted to {username}.")
                return func(*args, **kwargs)
            else:
                print(f"Access denied for {username}. Unauthorized user.")
        return wrapper

    return decorator

@authorize("Aryesh")
def secure_function():
    print("Executing secure function...")

if __name__ == "__main__":
    secure_function()
