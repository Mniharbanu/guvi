n1,n3=map(str,input().split())
if(len(n1)!=len(n1)):
  print("no")
x=[n1.count(i) for i in n1]
y=[n3.count(i) for i in n3]
if x==y:
  print("yes")
else:
  print("no")
