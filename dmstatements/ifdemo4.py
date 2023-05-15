maths =int(input("Enter your maths marks: "))
sci = int(input("Enter your science marks: "))
eng = int(input("Enter your english marks: "))

total = maths + sci + eng
print("Total marks: ", total)

per  = (total / 300) * 100
print("Percentage: ", per)
#70
#65
#91
#31
#72
#120

if per>=80: # 70 >= 80 false  # 65 >= 80 false # 91 >= 80 true # 31 >= 80 false
    print("Grade A")
elif per>=70: # 70 >= 70 true # 65 >= 70 false #  31 >= 70 false
    print("Grade B")    
elif per>=60: #65 >= 60 true  # 31 >= 60 false
    print("Grade C")
else:
    print("Fail")        