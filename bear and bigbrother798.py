def larger_year(a,b):
    years=0
    while a<=b:
        a*=3
        b*=2
        years+=1
    return years
a,b=map(int,input().split())
result=larger_year(a,b)
print(result)

