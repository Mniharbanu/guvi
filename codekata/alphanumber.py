n1=input()
k=[]
for x in n1:
  if(x.isnumeric()):
    k.append(x)
print(*k,sep='')
