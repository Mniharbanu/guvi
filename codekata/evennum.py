n1,n2=map(int,input().split())
if(n1<n2):
  for i in range(n1+1,n2,1):
     if i%2==0:
        print(i,end=' ')
