a=int(input().strip())
results=[]
for i in range(a):
    b=int(input().strip())
    if b>45:
        results.append(-1)
        continue
    digits=[]
    for digit in range(9,0,-1):
        if b>=digit:
            digits.append(digit)
            b-=digit
    if b!=0:
        results.append(-1)
    else:
        digits.sort()
        small_num=int(''.join(map(str,digits)))
        results.append(small_num)
for result in results:
    print(result)
