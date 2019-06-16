n1,m1=map(int,input().split())
def gcd(n1,m1):
    if(m1==0):
        return n1
    else:
        return gcd(m1,n1%m1)
a=gcd(n1,m1)
print(a)
