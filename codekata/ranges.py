in1,in2=map(int,input().split())
tt=[]
for i in range(in1,in2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        tt.append(i)
print(len(tt))
