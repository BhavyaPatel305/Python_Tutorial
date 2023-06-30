no1 = int(input("Enter no1: "))
no2 = int(input("Enter no2: "))

try:
    x = no1 / no2
    print("Result is", x)
except ZeroDivisionError:
    print("You cannot divide by zero")  

print("Bye")      

