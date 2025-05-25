#list creation

l1 = [1, 2, 3, 4]

l2 = list((1, 2, 3, 4, 5))
print(l2)

tup = ('chandan', 'rekha')
l3 = list("chandan")
print(l3)

l4 = list(tup)
print(l4)

l4.append("husky")
print(l4)
l4.remove('husky')
print(l4)
l4.pop(-1)
print(l4)

# indexing and slicing on list

l1 = [1, 2, 3, 4, 5]
print(l1[:])
print(l1[1:3])
print(l1[4:0:-1])

#indexing and slicing to write

l2 = [1, 2, 3, 4, 5]
l2[3] = 10
print(l2)

l3 = [1, 2, 3, 4, 5, 6]
l3[0:2] = [11, 12, 13, 14, 15] #only 0th and 1st index get replaced all others will be pushed to right
print(l3)

l4 = [1, 2, 3, 4, 5]
l4[0:3:1] = [11, 23, 122]
print(l4)

#list operations 1)concatination 2)Repetition 3)Membership 4)List comparision

l11 = [1, 2, 3, 4, 5]
l12 = [6, 7, 8]
l13 = l11 + l12
print(l13)
l14 = [1, 2, 3, 4]
l15 = [6, 7, 8]
l14.extend(l15)
print(l14)

#repition
l17 = [1, 2]
l18 = l17 * 2
print(l18)

print(3 not in l17)

print(l14 < l15) # it will compare element to element value in lists,

#list traversal

li1 = [1, 2, 3, 4]
for x in li1:
    print(x)
print("------------------------")
for x in range(len(li1)):
    print(li1[x], end=' ')
    print()

# Adding elements to list (List methods)-> 1)append 2)extend 3)insert 4)copy

l21 = [1, 2, 3, 4]
l21.append(55)
print(l21)

l22 = [1, 2, 3, 4, 5]
l22.extend([6, 7, 'Python'])
print(l22)

l21.extend('python')
print(l21)

l21[len(l21):] = [6, 7]
print(l21)

#deleting element from list 1)pop 2)remove 3)clear 4)del

l31 = [1, 2, 3, 4]
l31.remove(2)
print(l31)

l32 = [1, 2, 3, 4, 5]
l32.pop(1)
print(l32)

l32.clear()
print(l32)

del l32 #deletes the variable itself

del l31[0]
print(l31)

#Index, sort, reverse, count

l41 = [10, 5, 45, 5, 10, 20, 10]
print(l41.count(10))

l41.sort(reverse=True)
print(l41)

l42 = ['bat', 'cat', 'apple', 'Dog']
l42.sort(key=str.lower)
print(l42)

l43 = [10, 20, 30, 40]
l43.reverse()
print(l43)

l44 = ['apple', 'ball', 'chandan', 'RekhaMK']
l44.sort(key=str.lower)
print(l44)
l44.sort(key=len, reverse=True)
print(l44)

l45 = [10, 20, 30, 40, 50, 30]
print(l45.index(30))
print(l45.index(30, 3))

#List comprehension

L1 = [x for x in range(1, 10)]
print(L1)

L2 = [x*2 for x in range(1,4)]
print(L2)

L3 = [x.lower() for x in 'PythOn']
print(L3)

L4 = [int(x) for x in '1234']
print(L4)

L5 = [x for x in 'py6*t(hon' if x.isalpha()]
print(L5)
S1 = ''.join(L5)
print(S1)

print("adding for gitx")
print("this is code from last_prep guy")
print("done with modifying")
#git x u can start from here

print("i have added code from gitx side")
#last_prep guy u can start from here
#i have done addidng files from gitx side
#last_prep start urs

#coding done for develop branch
print("adding stuff to develop branch")



