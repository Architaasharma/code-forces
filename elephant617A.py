def elephant(x):
  step=x//5
  remainder=x%5
  if remainder!=0:
    step+=1
  return step
x=int(input())
print(elephant(x))
