num1,num2=input().split()
num1=int(num1)
num2=int(num2)
for i in range(num1+1,num2):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      print(i,end=' ')
  else:
    break
