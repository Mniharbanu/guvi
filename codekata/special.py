num=input()
a=0
for x in range (len(num)):
  if (num[x].isdigit() or num[x].isalpha() or num[x]==' '):
    continue
  else:
    a=a+1
print (a)
