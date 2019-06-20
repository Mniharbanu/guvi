x1=int(input())
mul=1
while(x1>0):
  di=x1%10
  mul=mul*di
  x1=x1//10
print(mul)
