l1,b1,h1=map(int,input().split())
surface=((2*l1*b1)+(2*b1*h1)+(2*h1*l1))
volume=l1*b1*h1
print(surface,end=' ')
print(volume)
