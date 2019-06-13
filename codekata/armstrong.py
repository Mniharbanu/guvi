num1,num2=map(int,input().split())
for i in range(num1+1,num2):
  x=0
  tem=i
  while(tem>0):
    d=tem%10
    x+=d**3
    tem//=10
  if(i==x):
    print(i,end=' ')
