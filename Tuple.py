t1 = (1, 2, 3, 4)
t2 = (1, 'chandan', 3.4, 1, 5+6j)
# Tuple once created cannot be modified
t3 = tuple([1, 2, 3, 4])
print(t3)
t4 = ()
t5 = (3,) #tuple cannot have single value, a ',' should be given if it has one value
t6 = 10, 11, 12 #parenthesis is not needed if multiple value are given to a variable
t7 = tuple("chandan")
print(t7)
t8 = tuple(range(1, 4))
print(t8)
print(t8[1]) # accessing the value of tuple(similar to list)

for x in t8:
    print(x)

#Tuple comprehension

T12 = (*(x for x in range(1,5)),)
print(T12)

T13 = (*(x*2 for x in range(1,4)),)
print(T13)
T14 = (*(x for x in 'Pyth*12o&N' if x.isalpha()),)
print(T14)
T15 = (*(x.lower() for x in 'PyThOn'),)
print(T15)
T16 = (*(int(x) for x in '1234'),)
print(T16)

# Indexing and Slicing on Tuple
# can only be done for reading purpose

T21 = (1, 2, 3, 4)
print(T21[0:2])
print(T21[0::2])
print(T21[::-1])
print(T21[3])
print(T21[-2])
print(T21[:])
print(T21[-1:-5:-1])
print(T21[-4:len(T21)])

#Packing Unpacking 1)concatination 2)Repetition 3)Packing Unpacking 4)Membership
T31 = (1, 2, 3)
T32 = (4, 5, 6)
T33 = T31+ T32
print(T33)

#Repetition
T34 =T31 * 2
print(T34)

T35 = 1,2,3,4,5 #packing makes it to a Tuple
print(T35)

a,b,c,d,e = T35
print(a,b,c,d,e) #Unpacking, here all the variables are assigned with each value in tuple

print(4 in T35) #membership

a,b,*c = T35
print(a, b, c) #by writing star before the variable all the remaining values are pushed as list




