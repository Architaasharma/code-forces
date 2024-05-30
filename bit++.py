a=int(input()) 
count = 0
for i in range(a):
    string=str(input())
    if string[0]== '+' or string[len(string)-1] == '+':
        count+=1
    elif string[0]== '-' or string[len(string)-1] == '-':
        count-=1
print(count)        
