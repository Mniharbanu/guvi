n1,n2=map(int,input().split())
num=n1*n2
for i in range(0,num+1):
  if(i**2==num):
    print('yes')
    break
else:
  print('no')
