def word(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case +=1
        elif i.islower():
            lower_case +=1
    if upper_case > lower_case:
        return s.upper()
    else:
        return s.lower()
s = str(input())
print(word(s))                  






