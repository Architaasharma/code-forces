def rearrange_sum(s):
    numbers = s.split('+')
    numbers.sort()
    result = '+'.join(numbers)
    return result
a = str(input())
print(rearrange_sum(a))
