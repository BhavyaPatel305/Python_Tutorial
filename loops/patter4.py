for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end=" ")
    print("\n")            


k=1
for i in range(1,6):
    #i=1
    #i=2
    #i=3
    for j in range(1,i+1):
        #j=1
        #j=1,2
        #j=1,2,3
        
        print(k,end=" ") #1 3
        k+=1 #k=2 , k=3, k=4, k=5, k=6, k=7, k=8, k=9, k=10
    print("\n")    
        

    