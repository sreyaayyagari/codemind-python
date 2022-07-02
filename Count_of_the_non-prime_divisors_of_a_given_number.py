def prime(n):
    if n==1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    else:
        return False
a=int(input())
c=0
for j in range(1,a+1):
    if a%j==0:
        p=j
        if prime(p):
            c+=1
print(c)         