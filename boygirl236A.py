a = str(input())
distinct_char=set(a)
num_distinct_char=len(distinct_char)
if num_distinct_char % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")