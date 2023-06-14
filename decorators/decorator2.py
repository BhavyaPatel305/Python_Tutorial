def throw_party(func):
    
    #func = eat_pizza
    def wrapper(a):
        print("Let's throw a party!",a)
        return func(a*10)
        # func()
    
    #wrapper(10)
    return wrapper
        


@throw_party
def eat_pizza(a):
    print("Let's eat pizza!")

eat_pizza(10)