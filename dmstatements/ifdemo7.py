#nested if else....

age= int(input("Enter a age: "))

if age>=18:
    print("You are eligible for voting")
    if age>21:
        print("You are eligible for marriage")
    else:
        print("You are not eligible for marriage but you can vote")
else:
    print("You are not eligible for voting")
    if age>14:
        print("You are eligible for school")
    else:
        print("You are not eligible for school")    
        

        