print("etner 1 for pizza")
print("etner 2 for burger")

no = int(input("Enter a number: "))
pizza = 0
crust = 0

if no==1:
    print("You have selected pizza")
    print("etner 1 for veg pizza")
    print("etner 2 for non veg pizza")
    pizza = int(input("Enter a pizza choice: "))
    if pizza==1:
        print("You have selected veg pizza")
        print("etner 1 for thin crust")
        print("etner 2 for thick crust")
        print("etner 3 for cheese burst")
        
        crust = int(input("Enter a crust choice: "))
        
        if crust==1:
            print("You have selected thin crust")
        elif crust==2:
            print("You have selected thick crust")
        elif crust==3:
            print("You have selected cheese burst")
        else:
            print("You have selected wrong option")    
                            
    else:
        print("You have selected non veg pizza")   
        
        crust = int(input("Enter a crust choice: "))
        
        if crust==1:
            print("You have selected thin crust")
        elif crust==2:
            print("You have selected thick crust")
        elif crust==3:
            print("You have selected cheese burst")
        else:
            print("You have selected wrong option")    

elif no==2:
    print("You have selected burger")

else:
    print("You have selected wrong option")        
