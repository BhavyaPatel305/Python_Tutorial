#//condition ---> true or false
#true --> store.. 
# list --> names --> len >=3 'c' --> >3

li = [5,7,22,97,54,62,77,23,73,61]
fl = list(filter(lambda x:(x%2==0),li))
# for i in li:
#     if i %2 == 0:
#         fl.append(i)

print(fl)        
        