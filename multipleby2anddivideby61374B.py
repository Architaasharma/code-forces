a=int(input())
result=[]
for i in range(a):
    b=int(input())
    orignal_n = b
    count2,count3=0,0
    while b%2==0:
        b//=2
        count2+=1
    while b%3==0:
        b//=3
        count3+=1
    if b!=1:
        result.append("-1")
    else:
        if count3>=count2:
            result.append(str(count3+(count3-count2)))
        else:
            result.append("-1")
print("\n".join(result))

