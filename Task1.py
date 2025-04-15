#Task 1: Calculate Factorial Using a Function

num = int(input("Enter Number: "))
def fact(a):
    FACT = 1
    while a > 0:
        FACT *= a
        a -= 1
    return FACT

result = fact(num)
print(f"Factorial of {num} is: {result}")