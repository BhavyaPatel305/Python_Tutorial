name = input("Enter your name: ")

try:
    flag = name.isalpha()
    if not flag:
        raise ValueError("You cannot enter only alphabets")


except ValueError as e:
    print(e)        

else:
    name = name.upper()
    print("You entered", name)        
    