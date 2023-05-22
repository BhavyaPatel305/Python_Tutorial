no = 153

rem = 0
sum =0
#153 > 0 True
#15 > 0 True
#1 > 0 True
while no>0:
    #3 = 153 % 10 rem = 3
    #5 = 15 % 10 rem = 5
    #1 = 1 % 10 rem = 1
    rem = no % 10
    #0 = 0 + 3*3*3 = 27
    #27 = 27 + 5*5*5 = 152
    #152 = 152 + 1*1*1 = 153
    sum = sum + rem * rem * rem
    #153 = 153 // 10 = 15
    #15 = 15 // 10 = 1
    #1 = 1 // 10 = 0
    no = no//10


print("Sum is",sum)    
    