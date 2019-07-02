a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
for k in range(0,a1[1]):
  a2=[a2[-1]] + a2[:-1]
print(*a2,end=' ')
