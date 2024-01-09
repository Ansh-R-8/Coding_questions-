'''Q Given a sentence interchange the between the word 'and'.
Input Size : |S| <= 1000000
Sample Testcase :
INPUT
jack and jill went up and down to get water
OUTPUT
jill and jack went down and up to get water'''

# Code
inp = input().split()
for i in range(1,len(inp)):
    temp = ''
    if inp[i] == 'and':
        temp = inp[i-1]
        inp[i-1] = inp[i+1]
        inp[i+1] = temp
print(' '.join(map(str,inp)))

'''Q Given a string S ,print the vowels first and then consonants in the same order as they have occurred in the string.
Input Size : N <= 10000
Sample Testcase :
INPUT
GoAt
OUTPUT
oAGt'''

#code
inp = input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
out = ''
for char in inp:
    if char in vowels:
        out += char
for char in inp:
    if char not in out:
        out += char
print(out)
