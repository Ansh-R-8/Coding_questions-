'''Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
Input Size : N <= 100000
Sample Testcase :
INPUT
5 2
1 2 3 4 5
OUTPUT
yes
'''

# code
n , k = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = len(arr) - 1 # Bianry search
while l <= r:
    mid = (l+r) // 2
    if arr[mid] == k:
        print('yes')
        break
    elif arr[mid] < k:
        l = mid + 1
    else:
        r = mid - 1
else:
    print('no')
    
