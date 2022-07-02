def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
for i in range(1,100):
    r=m+n+i
    if prime(r):
        print(i)
        break