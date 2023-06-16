
user = {"name":"surya","password":"surya123"}

def loginRequired(func):
    
    def checkUser(username,password):
        if username == user["name"] and password == user["password"]:
             return func()
        else:
            return False

    return checkUser

@loginRequired
def getData():
    #print("I am getting data...")
    return True


x = getData("surya","surya123")
if x:
    print("I am getting data...")
else:
    print("Please login first...")    
