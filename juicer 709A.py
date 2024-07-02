n,b,d=map(int,input().split())
oranges=list(map(int,input().split()))
waste=0
count=0
for orange in oranges:
    if orange<=b:
        waste+=orange
        if waste>d:
            count+=1
            waste=0
print(count)
    