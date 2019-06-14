a=int(input())
n=list(map(int,input().split()))
if (a==len(n)):
  n.sort()
  medi=a//2
print(n[medi])
