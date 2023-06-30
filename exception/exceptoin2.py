try:
    age = int(input("Enter your age: "))
    print("Age entered is", age)
except ValueError:
    print("You must enter an integer value for age")
except:
    print("Some error occured")
        