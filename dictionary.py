l1 = ['chandan', 'husky']
dict8 ={x:y for x, y in enumerate(l1,1)}
print(dict8)

d1 = {'A':'Apple', (1,2,3):'chandan'}
for i in d1:
    print(i, d1[i])

d2 = {1:[1,2,4], 2:('apple', 'ball', 'cat')}
for x in d2:
    print(x, d2[x])

print("------Dictionary creation------------")

# using iterator pairs

l1 = [('name','chandan'), [1, 'one'], (33, 'age')]
d2 = dict(l1)
print(d2)

#using zip function
x = [1, 2, 3, 4]
y = ('one', 'two', 'three')
d3 = dict(zip(x,y))
print(d3)

#using enumerate function
login = ('chandan', 'rekha','husky')
d3 = dict(enumerate(login, start=1))
print(d3)

# creation using comprehension
print("-----------comprehension--------------------")
l1 = ['no_1', 'no_2', 3, 4]
l2 = ['one', 'two', 'three']
d5 = {x:y for x, y in zip(l1, l2)}
d6 = dict(zip(l1,l2))
print(d5)
print(d6)

d6 = {x:y for x, y in enumerate(l2, start=1)}
print(d6)

l4 = [('one', 1), ('two', 2), (3,'three')]
d7 = {x:y for x, y in l4}
print(d7)

#loping over dictionary
print(d7.values())
for i in d7.values():
    print(i)
print("-000-------000----")
print(d7.items())
print(type(d7.items()))
for i in d7.items():
    print(i)
for x, y in d7.items():
    print(x, y)

# looping over dictionary

print(d7.get(5))
print(d7.setdefault(5, 'undifined'))
print(d7)

print(d7.get(7))

d7 = {'Husband':'Chandan', 'wife':'Rekha'}
d8 = {'Baby':'Sidharth', 'Baby_g':'Mira'}
print("---------------")
d7.update(d8)
print(d7)

d8 = d7.copy()
print(d8)

print(d8.pop('Baby_g'))
print(d8)
print(d8.popitem())
print(d8)
print(d8.clear())
print(d8)