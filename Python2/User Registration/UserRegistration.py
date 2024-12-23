import re

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_user_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class UserRegistrationSystem:
    def __init__(self):
        self.user_database = []

    def is_valid_email(self, email):
        try:
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if re.match(email_regex, email):
                return True
            else:
                raise ValueError("Invalid email format.")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def is_unique_email(self, email):
        return all(user.email != email for user in self.user_database)

    def register_user(self):
        print("\n=== User Registration ===")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        if not self.is_valid_email(email):
            return

        if not self.is_unique_email(email):
            print("Error: Email is already registered.")
            return

        new_user = User(name, email, password)
        self.user_database.append(new_user)
        print("Registration successful!")

    def display_registered_users(self):
        print("\n=== Registered Users ===")
        if not self.user_database:
            print("No users registered.")
        else:
            for user in self.user_database:
                user.display_user_info()
                print("------------------")

if __name__ == "__main__":
    system = UserRegistrationSystem()

    while True:
        print("\n1. Register User")
        print("2. Display Registered Users")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.register_user()
        elif choice == "2":
            system.display_registered_users()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
