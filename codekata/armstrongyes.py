def armst():
  x=0
  temp=number
  while(temp>0):
    c=temp%10
    x+=c**3
    temp//=10
  if(number==x):
    print('yes')
  else:
    print('no')
number=int(input())
armst()
