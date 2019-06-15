num=input()
list=['a','e','i','o','u']
for x in num:
  if(x in list):
    print('yes')
    break
else:
  print('no')
