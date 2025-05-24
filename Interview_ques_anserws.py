#print star
print("---------star--------------")
def star(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=' ')
        for k in range(1, i*2):
            print('*', end=' ')
        print(' ')
star(5)

s1 = 'chan23d827a**n'
s2 = []
s3 = [' ']
for i in s1:
    if i.isalpha():
        s2.append(i)
    else:
        if i.isdigit():
            s3.append(i)
ans = s2 + s3
print(''.join(ans))

s4 = 'chndn@gmail.com'
print(s4.split('@')[0])

#vowel count
print("-----------vowel count--------------")
s1 = 'Chandan is a tester'
vowels = 'aeiou'
cnt = {i:s1.count(i) for i in s1 if i in vowels }
print(cnt)

a = [0, 3, 4, 7]
b = ['q','w', 'r', 't']

d = dict(zip(a, b))
d1 = {a:b for a,b in zip(a,b)}
print(d1)
print(d)

print('--------adding two list items of uneven digits--------------')
d = [1, 2, 3, 4]
m = [2, 3, 4, 5, 6]
r = []
if len(d) != len(m):
    d.append(0)
for i in range(len(d)):
    r.append(d[i]+m[i])
print(r)

#python prog to find most occuring character and count

s1 = 'landing'
cnt = {i:s1.count(i) for i in s1}
print(cnt)
keys = list(cnt.keys())
values = list(cnt.values())
print(keys, values)
occ=max(values)
ele=keys[values.index(occ)]
print(ele,occ)

print('count of substring of a string')
def count_all_substrings(s):
    n = len(s)
    return n * (n + 1) // 2

# Example usage
input_string = "abc"
print("Total substrings:", count_all_substrings(input_string))

print('----no of spaces in string--------')

s = 'chandan is a boy'
print(s.count(' '))

print('----no of character in string----')
s1 = 'chandan'
s2 = list(s1)
print(s2)
print(f'no of character is {len(s2)}')
count = 0
for i in s1:
    count = count+1
print(count)
print('check if string contains number')

s1 = 'chand2an'
for i in s1:
    if i.isdigit():
        print(f'yes the no is {i}')

a= [1,2,3,4]
sums = 0
for i in a:
    sums= sums+i
print(sums)

t1 = (1, 2, 3, 4)
l2= [1,3,4,66]
l1 = [t1]
t2 = (l2,)
print(l1)
print(t2)

l1 = [1, 2, 3, 4]
l1[0], l1[-1] = l1[-1], l1[0]
l1[1], l1[2] = l1[2], l1[1]
print(l1)
print(l1)

d1  = {'a':'apple', 'b':'ball'}
print(d1.items())
rd1 = {}
for keys, values in d1.items():
    rd1[values] = keys
print(rd1)



s1 = 'c9and3a1n'
for i in s1:
    if ord(i) in range(48, 58):
        print(f'yes the no is {i}')