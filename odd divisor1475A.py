a = int(input())
result=[]
for i in range(a):
    n=int(input())
    if n & (n - 1) == 0:
        print("NO")
    else:
        print("yes")
