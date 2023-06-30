#custome exception we need to create one class which is inherited from Exception class
# class InvalidAgeException(Exception):
#     pass

from invalidAgeEx import InvalidAgeException

try:
    age = int(input("Enter your age: "))
    if age<18:
        raise InvalidAgeException("You are not allowed to vote....")
    
    else:
        print("You are allowed to vote")

except InvalidAgeException as e:
    #print("You are not allowed to vote")        
    print(e)
