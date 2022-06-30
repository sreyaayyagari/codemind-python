n=int(input())
t=n
if n<0:
    n=abs(n)
l=len(str(n))
s=0
for i in range (1,l+1):
    r=n%10
    s=s*10+r
    n=n//10
if t<0:
    s=-abs(s)
print(s)