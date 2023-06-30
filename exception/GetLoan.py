
from LoanCriteriex import LoanFailedException
salary = float(input("Enter your salary: "))

try:
    if salary<0:
        raise ValueError("Salary cannot be negative")
    elif salary< 1000:
        raise LoanFailedException("You are not eligible for loan")

except ValueError as e:
    print(e)    
    