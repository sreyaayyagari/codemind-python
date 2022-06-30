n=int(input())
l=len(str(n))
p=1
s=0
for i in range(1,l+1):
    r=n%10
    s=s+r
    p=p*r
    n=n//10
print(p-s)
