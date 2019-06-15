num=list(input())
if len(num)%2==0:
    num[int(len(num)/2)] ='*'
    num[int(len(num)/2)-1]='*'
else:
    num[int(len(num)/2)] ='*'
for x in range(0,len(num)):
    print(num[x],end='')
