n1=int(input())
re=0
while(n1>0):
  digit=n1%10
  re=re*10+digit
  n1=n1//10
print(re)
