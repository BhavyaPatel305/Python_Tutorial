no =123
rem =0
sum =0
mul =1

while no >0:
    rem = no % 10
    sum = sum + rem
    mul = mul * rem
    no = no // 10


if sum == mul:
    print("Special")

else:
    print("Not Special")        