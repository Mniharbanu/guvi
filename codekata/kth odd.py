a1,b1=map(int,input().split())
li=list(map(int,input().split()))
l=[]
for i in range(0,len(li)):
  if li[i]%2!=0:
    l.append(li[i]) 
print(l[b1-1])




