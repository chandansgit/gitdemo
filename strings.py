s1 = "chandan"
for x in s1:
    print(x)

for i in range(len(s1)):
    print(s1[i])

#string literals
s1 = 'hello'
s2= "hello"
s3 = """ chandan
is a good boy
person"""

for c in s3:
    print(c)

#indexing and slicing
print("---------------------------")
#string indexing
s21 = "hello"
print(s21[0])
print(s21[-5])
print(s21[::-1])
#s21[0] = 'M', error, cannot replace once created
#whenever your modifying with concatenation etc it will give new string
s22 = "chandan is a man"
print(s22[:7])
print(s22[:])
print("----------------------------------")
#Operation on strings
#1) concatination 2)repetition 3)Membership 4)String Comparision

s1='ram'
s2 = 'sham'
print(s1+s2)

print(s1*2)
print('r' in s1)
print(s1 < s2)

print("------------")
#Class String

print(dir(s1))
print(s1.__sizeof__())

#string methods
s3 = "hello how are you"
print(s3.find('h',0,len(s3)))
print(s3.find('o',5,len(s3)))
print(s3.rfind('h',0,len(s3)))
#gives -1 if string is not found

#Index, same as find but throws error if string is no found
print(s3.index('o'))
print(s3.index('how'))
#print(s3.index('man')) throws error
print(s3.rindex('o'))
print(s3.rindex('o', 0, 15))

#count
print(s3.count('o'))
print(s3.count('o', 5))

#allignment and padding
print("-------------------------")
s1 = 'hello'
s2 = s1.ljust(10, '*')
print(s2)
s3 = s1.rjust(10, '*')
print(s3)
s4 = s1.center(10, '*' )
print(s4)
s5 = s1.zfill(10)
print(s5)

#strip methods
s0 = '      Hello'
s11 = s0.strip()
print(s0)
print(s11)
s1 = '-----Hello'
print(s1)
s2 = s1.lstrip('-')
print(s2)
s3 = '****Hello****'
print(s3)
s4 = s3.strip('*')
print(s4)

s22 = "#&^chand^an)("
s23 = s22.strip('#&^()')
print(s23)

#Join And Split 1)replace 2)join 3)split 4)rsplit 5)splitlines
s31 = 'a-b-c-d'
s32 = s31.replace('-', ',')
s37 = s31.replace('-', '')
print(s37)
print(s32)
s33 = s31.replace('-', '*', 2)
print(s33)
s34 = "chandan@yahoo.com"
s35 = s34.replace('yahoo', 'gmail')
print(s35)
#join
print("---------------------------")

s1 = 'xyz'
s2 = 'abc'
s3 = s1.join(s2)
print(s3)

s1 = '/'
s2 = 'abc'
s3 = s1.join(s2)
print(s3)

s21 = ['a','b','c']
s22 = ''.join(s21)
print(s22)

#split , splits the string based on character specified and places them in list if nothing given then splits space
print("-------------")
s1 = "chandan s m"
s2 = s1.split('s')
print(s2)


#Prefix and Suffix
s1 = 'Python is very easy'
s2 = s1.startswith('is', 7)
print(s1.endswith('easy'))
print(s2)
s3 = s1.removeprefix('Py')
print(s3)
s4 = s1.removesuffix('easy')
print(s4)

s1 = 'python was hard'
s2 = s1.partition('was') # this will give tuple
print(s2)






