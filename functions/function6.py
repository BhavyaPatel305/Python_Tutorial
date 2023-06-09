#return student name who is having highest marks
def students(st):
    max = 0
    name =""
    print(st)
    for i,j in st.items():
        if j > max:
            max = j
            name = i
    
    return name    



st ={'raj':20,'ram':30,'ravi':40}
x = students(st)
print(x)
    


    
