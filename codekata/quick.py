a=int(input())
n=list(map(int,input().split()))
x=sorted(n)
for i in range(0,len(x)):
  print(x[i],end=' ')
