try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise ValueError("You are not allowed to vote")

except ValueError as e:
    print(e)
    
except:
    print("Some error occured")        