#lambda function (anonymous function)

k = lambda x: x * 2
print(k(2))

r = lambda x,y: x + y
print(r(4, 5))

print((lambda x, y: x + y)(5,6))

#lambda fun to create list from a list

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = list(filter(lambda x: x % 3==0, l1))
#l2 = list(f)
print(f)

#map
l1 = [1, 2, 3, 4]
l2 = list(map(lambda x: x*2,l1))
print(l2)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l4 = list(map(lambda x: x if x % 2== 0 else -x, l3))
print(l4)

#print tables
l1 = [10, 20]
l2 = [30, 40]
k  =list(map(lambda x, y: x + y , l1,l2))
print(k)
print(l1 + l2)

n=[5]
table = list(map(lambda x,y: x*y, list(range(1,11)), n*10))
print(table)








x = lambda z, y: z * y
print(x(2, 3))


l1 = [1, 2, 3, 4, 5, 6]

res = list(filter(lambda x: x % 2== 0, l1))
print(res)
