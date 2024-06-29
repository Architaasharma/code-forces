t=int(input())
for _ in range(t):
    n=(input().strip())
    min_step=len(n)
    for target in["00","25","50","75"]:
        index=1
        steps=0
        for i in range(len(n)-1,-1,-1):
            if n[i]==target[index]:
                index-=1
                if index<0:
                    break
            else:
                steps+=1
        if index<0:
            min_step=min(min_step,steps)
    print(min_step)

