#set is collection of distinct heterogeneous unordered elements and it is mutable
s1 = {3} # must have at least one element
s5 = set([1, 2, 3, 4])
s6 = set("chandan")
print(f'the elements of set is {s6}')
print(s5)
print(type(s1))

s2 = {10, 20, 30, 40, 50}
print(s2)
for x in s2:
    print(x)

s2.add(55)
print(s2)
s2.remove(55)
print(s2)

s3 = {1, 2, 'string', (1, 2, 3)}
print(s3)

s4 = {1, 1, 2, 3, 2, 4, 5}
print(s4)
# Sets in mathematics

s = {1,2,3,4,5,6,7,9,10}
a = {1,2,3,5,7} #a is a subset of s or s is a super set of a or a is proper subset of s
b = {5,7,9,10}  #b is a subset of s or s is a super set of b
c = {1,2,3,4,5,6,7,9,10} #c is equal to s or c is subset of s


#set operations 1) union 2)intersection 3)intersection_update 4)difference 5)difference_update
#6)symmetric_difference 7)symmetric_difference_update
s01 = {1, 2, 3, 5, 7}
s11 = {1, 2, 3, 5, 7}
s12 = {5, 7, 9, 10 ,11}
s13 = s11.union(s12)
print(s13)
s15 = s11.intersection(s12)
print(s15)
s11.intersection_update(s12) # this will modify the s11 as we are calling update on it
print(s11)
s21 = s01.difference(s12) #common element in s12 is removed from s01 and placed in s21={1,2,3}
print(s21)
#s01.difference_update(s12) this will update s01 to {1,2,3}
s22 = s01.symmetric_difference(s12) # picks only unique element from both sets, common are ignored{1,2,3,9,10,11}
print(s22)
#s01.symmetric_difference_update(s12) this will update s01 to {1,2,3,9,10,11}

#Operators on set
#All the above operations are supported with operators
#1)union | 2)intersection & 3)intersection_update &= 4)difference - 5)difference_update -=
#6)symmetric_difference ^ 7)6)symmetric_difference_update ^=
#eg s3 = s1|s2

#Adding and deleting elements
s1 = {1,2,3}
s1.add(4)
print(s1)
s1.update([8,9,10])
print(s1)
s2 = s1.copy()
print(s2)
#Deleting---------------------------------------

s4 = {1,2,3,4}
s4.pop()
print(s4)
s4.discard(4)
print(s4)
s4.clear()
print(s4)
s5={1,2,3,4}
s5.remove(2)
print(s5)


#done to check develop branch



