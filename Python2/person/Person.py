class Person:
    def __init__(self,name, age):
        self.name = name
        self.age=age

    # def displayDetails(self):
    #     print(f"Name : {self.name}")
    #     print(f"Age : {self.age} years old")

obj1= Person("Alice", 25)
obj2= Person("Bob",30)

# obj1.displayDetails()
# obj2.displayDetails()

print(f"Name : {obj1.name} , Age : {obj1.age}")
print(f"Name : {obj2.name} , Age : {obj2.age}")
