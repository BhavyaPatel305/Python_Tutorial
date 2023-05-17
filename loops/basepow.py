base = int(input("Enter the base:"))    
pow = int(input("Enter the pow:"))    
x =1
#print(base**pow)
#2
#5
for i in range(1,pow+1):

    # 1 = 1 * 2 x = 2
    # 2 = 2 * 2 x = 4
    # 4 = 4 *2 x = 8
    #8 = 8 * 2 x = 16
    #16 = 16 * 2 x = 32  
    x = x * base

print(base," ^ ",pow," = ",x)    