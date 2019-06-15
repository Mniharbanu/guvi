num1,num2=map(int,input().split())
l=list(map(int,input().split()))
co=0
for i in l:
  if(i==num2):
    co=co+1
print(co)
