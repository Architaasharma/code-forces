n , k = map(int , input().split())
nums = list(map(int, input().split()))
count = 0
if k<= n:
    for i in range(n):
        if nums[i] >= nums[k-1] and nums[i] > 0:
            count += 1
print(count)    