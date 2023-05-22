for i in range(5):

    #3-0 =3,0,-1
    #3-1 =2,0,-1
    #3-2 =1,0,-1
    for j in range(5-i,0,-1):
        print(" ", end = "")
    for k in range(i+1):
        print("* ",end="")
    print("\n")