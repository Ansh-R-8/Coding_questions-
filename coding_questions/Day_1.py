'''You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.
Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.
Output Description:
Print the difference of indices of largest and smallest array'''

# My code
n = int(input())
arr = list(map(int, input().split()))

max_num = 0
max_ind = 0
min_num = float('inf')
min_ind = 0

for ind,num in enumerate(arr):
    if num > max_num:
        max_num = num
        max_ind = ind
    if num < min_num:
        min_num = num
        min_ind = ind

res = max_ind - min_ind
print(res)
