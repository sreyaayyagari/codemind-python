n=int(input())
t=n
s=0
l=len(str(n))
for i in range(l,0,-1):
    r=n%10
    s=r**i+s
    n=n//10
if s==t:
    print(True)
else:
    print(False)
    