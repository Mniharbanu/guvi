x,y=input().split()
x=int(x)
y=int(y)
t=0
array = [int(i) for i in input().split()]
for a in range (0,y):
    t=t+array[a]
print(t)
