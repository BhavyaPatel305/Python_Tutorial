digits =[]

while True:
    no =int(input("Enter a number: "))
    digits.append(no)
    flag =int(input("Do you wish to add more numbers? 0-No 1-Yes"))
    if flag ==0:
        break

evensum =0
oddsum =0

for i in digits:
    if i %2 ==0:
        evensum +=i
    else:
        oddsum +=i


print("Even sum is: ",evensum)
print("Odd sum is: ",oddsum)            



maxim = digits[0]
minm = digits[0]
[12,33,44,6,7,89,1]


for i in digits:
    #  12 > 12 F als
    #  33 > 12 T
    #  44 > 33 T
    #  6 > 44 F
    #  7 > 44 F
    #  89 > 44 T
    #  1 > 89 F
    if i > maxim:
        # 33
        # 44
        # 89
        maxim = i
        # 12 < 12 False
        # 33 < 12 False
        # 44 < 12 False
        # 6 < 12 True
        # 7 < 6 False
        # 89 < 6 False
        # 1 < 6 True
    if i < minm:
        # 6
        # 1
        minm = i

print("Maximum is: ",maxim)
print("Minimum is: ",minm)        




