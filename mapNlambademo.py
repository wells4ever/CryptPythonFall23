def cube(n):
    return n*n*n

list1 = list(range(-5,5)) #initial list

list2 = list(map(cube, list1)) #list using map of defined function

list3 = list(map(abs, list2)) #list of absolute values of list 2

list4 = list(map(lambda n: n*n*n, list1)) #eliminate separate function definition if able to concisely define

list5 = [x ** 3 for x in list1 ] #allow generation of list using for loop inside bracket

list6 = [(x,x**3) for x in list1] #list of tuples of x & x^3

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
