'''Q Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
Input Size : N <= 1000
Sample Testcase :
INPUT
5
code
overload
vishal
sundar
anish
OUTPUT
yes
'''

# Solution_:
n = int(input())
for i in range(n):
    arr = [input()]
Flag = True
vowels = ['a','e','i','o','u']
for char in arr:
    if not any(let in vowels for let in char):
        Flag = False
        break
if Flag:
    print('yes')
else:
    print('no')
