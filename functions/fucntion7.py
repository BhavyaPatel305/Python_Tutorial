def reverse(a):
    reversed_list = []
    #
    for i in a:
        #11,12
        num = i
        #
        reversed_num = 0
        while num>0:
            digit = num % 10 #1
            reversed_num = reversed_num * 10 + digit
            num //= 10
        reversed_list.append(reversed_num)

    return reversed_list

l1 = [11, 12, 13, 14, 15]
print(reverse(l1))