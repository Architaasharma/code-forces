a=int(input().strip())
result=[]
for i in range(a):
    b=int(input().strip())
    k=2
    while True:
        power=(1<<k)-1
        if b%power==0:
            x=b//power
            result.append(x)
            break
        k+=1
for results in  result:
    print(results)

