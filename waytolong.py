a=int(input())

for i in range(a):
    str=input()
    if len(str)>10:
        length =len(str)
        length-=2
    
        first_letter=str[0]
        last_letter=str[length+1]

        print("{}{}{}".format(first_letter,length,last_letter))
    else:
        print(str)    