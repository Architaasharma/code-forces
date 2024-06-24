n=int(input().strip())
s=input().strip()
count={}
for i in range(n-1):
    two_gram= s[i:i+2]
    if two_gram in count:
        count[two_gram]+=1
    else:
        count[two_gram]=1
max_gram=max(count,key=count.get)
print(max_gram)

