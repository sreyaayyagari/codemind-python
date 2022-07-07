n=int(input())
p1=n*n
l=len(str(n))
s=0
for i in range(1,l+1):
    s=s*10+n%10
    n=n//10
r=s*s
l1=len(str(r))
m=0
for j in range(1,l1+1):
    m=m*10+r%10
    r=r//10
if m==p1:
    print(True)
else:
    print(False)