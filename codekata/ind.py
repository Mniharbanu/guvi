n1=int(input())
ip4=list(map(int,input().split()))
srt=ip4[:]
srt.sort()
for i in range(0,len(ip4)):
  if(ip4[i]!=srt[i]):
     print(i)
     break
