n=int(input())
a=n
i=len(str(n))
s=0
while n:
    r=n%10
    s=s+r**i
    i-=1
    n=n//10
if s==a:
    print(True)
else:
    print(False)
    