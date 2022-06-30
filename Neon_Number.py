n=int(input())
p=n*n
l=len(str(p))
s=0
for i in range(1,l+1):
    r=p%10
    s=s+r
    p=p//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")