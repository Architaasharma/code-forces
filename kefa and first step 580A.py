a=int(input())
n=list(map(int,input().split()))
max_len=1
current=1
for i in range(1,a):
    if n[i]>=n[i-1]:
        current+=1
    else:
        current=1
    max_len=max(max_len,current)
print(max_len)

