import re

class Password:

    def __init__(self):
        self.score=0

    def check_password_strength(self,password):
        length=len(password)>=8
        uppercase=re.search(r"[A-Z]", password) is not None
        lowercase=re.search(r"[a-z]", password) is not None
        digit=re.search(r"\d", password) is not None
        special_characters= re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

        if length:
            self.score += 1
        if uppercase:
            self.score += 1
        if lowercase:
            self.score += 1
        if digit:
            self.score += 1
        if special_characters:
            self.score += 1

        return self.score
    

    def main(self):
        password= input("Enter your password: ")

        score = self.check_password_strength(password)

        if score == 5:
            print("Password strength: Your password is strong.")
        elif score >= 3:
            print("Password strength: Your password is medium strength.")
        else:
            print("Password strength: Your password is weak.")

if __name__ == "__main__":
    obj=Password()
    obj.main()
