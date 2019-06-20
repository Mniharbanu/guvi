a1,b1,c1=map(int,input().split())
ap=0
for x in range(1,c1+1):
 ap+=a1+(c1-x)*b1
print(ap)
