import math_operations as mt

def operations():
    n1= float(input("Enter the first number: "))
    n2=float(input("Enter the second number: "))

    print(f"Addition : {mt.add(n1,n2)}")
    print(f"Subtraction : {mt.subtract(n1,n2)}")
    print(f"Multiplication : {mt.multiply(n1,n2)}")
    try:
        result = mt.divide(n1,n2)
        print(f"Division : {result}")
    except ValueError as e:
        print(e)

    print(f"Power : {mt.power(n1,n2)}")


operations()

result = mt.add(mt.multiply(2, 3), mt.subtract(10, 4))
print(f"Combined Operation: (2 * 3) + (10 - 4) = {result}")