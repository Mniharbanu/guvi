val=input()
a1=[val[i] for i in range(len(val)) if i%2==0]
a2=[val[i] for i in range(len(val)) if i%2!=0]
for j in range(len(val)//2):
  print(a2[j]+a1[j],end="")
