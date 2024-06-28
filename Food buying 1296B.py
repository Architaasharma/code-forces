a = int(input())
results=[]
for i in range(a):
    n=int(input())
    total_spent=0
    while n>=10:
        spend=(n//10)*10
        cashback=spend//10
        total_spent+=spend
        n=n-spend+cashback
    total_spent += n
    print(total_spent)

