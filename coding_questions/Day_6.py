'''Q Rajesh was going through alternative array sorting. He wishes to print the array alternatively. Hence hired you. 
Your task is to help rajesh in printing the array alternatively.


An alternative array is an array in which first element is maximum of the whole array second element is minimum of the whole array. 
Third element is the second largest. Fourth element is the second smallest And so on. print the array in the desired manner.


Input Description:
You are given with the length of array ‘n’. followed by ‘n’ space separated numbers.

Output Description:
Print the array as mentioned.

Sample Input :
5 1 7 11 16 19
Sample Output :
19 1 16 5 11 7'''

# code
lenh = int(input())
arr = list(map(int, input().split()))
res = []
half = len(arr)//2
for i in range(half):
    max_n = max(arr)
    min_n = min(arr)
    res.append(max_n)
    res.append(min_n)
    arr.remove(max_n)
    arr.remove(min_n)
    max_n = 0
    min_n = 0
if arr:
    x = arr[0]
    res.append(x)
print(' '.join(map(str, res)))
    
