
a = input().strip()  
t = input().strip()  
key = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]
shift = {}
if a == 'L':
    for row in key:
        for i in range(len(row) - 1):  
            shift[row[i]] = row[i + 1]
elif a == 'R':
    for row in key:
        for i in range(1, len(row)):  
            shift[row[i]] = row[i - 1]
original_message = ''.join(shift[char] for char in t)
print(original_message)


