num=int(input())
n1,n2=map(int,input().split())
for x in range(n1+1,n2):
  if(x==num):
    print('yes')
    break
else:
  print('no')
