N=int(input())
temp=N
rev=0
while(N>0):
  digit=N%10
  rev=rev*10+digit
  N=N//10
if(temp==rev):
  print("yes")
else:
  print("no")
