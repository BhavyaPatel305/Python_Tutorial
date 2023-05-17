evensum = 0
oddsum = 0

for i in range(1,20):
    #1 false
    #2 true
    #3 false
    #4 true
    if i %2 ==0:
        print("even =",i) # even = 2 #even = 4
        evensum = evensum + i
        #0 = 0 + 2 = 2
        #2 = 2 + 4 = 6
    else:
        print("odd =",i) # odd = 1 #odd = 3
        oddsum = oddsum + i
        #0  = 0 + 1 = 1
        #1 = 1 + 3 = 4

print("even sum",evensum)
print("odd sum",oddsum)            