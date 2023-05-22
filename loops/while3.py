no =121
temp = no
rem =0
sum=0

#123 > 0 True
#12 > 0 True
#1 > 0 True
#0 > 0 False
while no>0:
    #0 = 123 % 10 rem = 3
    #3 = 12 % 10 rem = 2
    #2 = 1 % 10 rem = 1
    rem = no % 10
    # 0 = 0 * 10 + 3 = 3 sum = 3
    # 3 = 3 *10 +2 = 32 sum = 32
    #32 = 32 * 10  + 1 = 321 sum = 321
    sum = sum * 10 + rem
    #123 = 123 // 10 = 12
    #12 = 12 // 10 = 1
    #1 = 1 // 10 = 0
    no = no//10
    
print("Reverse is",sum) 

if sum == temp:
    print("Palindrome")
else:
    print("Not Palindrome")       