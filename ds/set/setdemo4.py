# d = set({1,34,67,89,90,34,1,90,78})
# l = list(d)
# l.sort()
# print("second larget element is",l[-2])


set1 = set({45,67,89,90})
set2 = list(set1)
max = set2[0]
#89
print(set2)

for i in set2:
    #  (89<89)
    if (max<set2[i]):
        # max = 
        max = set2[i-1]

print(max)
print(set2[i-2])