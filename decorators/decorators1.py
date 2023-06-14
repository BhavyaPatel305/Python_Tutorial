# '''
# 1) in python we can define a function inside another function
# 2) in python we can pass a function as an argument to another function
# '''

# def welcomeGreet(str):
    
#     def addWelcomeGreet():
#         return "Welcome to "
    
#     return addWelcomeGreet() + str

# def site(sitename):
#     return sitename

# print(welcomeGreet(site("www.google.com")))

#site
def decorator_message(fun):
    
    print(fun) #site
    def addWelcomeGreet(sitename):
        return "Welcome to " + fun(sitename)
    
    return addWelcomeGreet


@decorator_message
def site(site_name):
    # www.google.com
    print("site...",site_name)
    return site_name

print(site("www.google.com"))