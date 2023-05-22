no1 = 0
no2 = 1
sum = 0
print(no1)
print(no2)
for i in range(1,8):
    #0  0 + 1 = 1
    #1  1 + 1 = 2
    #   1 +2 = 3
    #   2 + 3 = 5
    sum = no1 + no2
    print(sum)
    #no1 = 1
    #no1 = 1
    #no1 = 2
    
    no1 = no2
    #no2 = 1
    #no2 = 2
    #no2 = 3
    no2 = sum
    
    