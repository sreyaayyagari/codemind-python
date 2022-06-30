n=int(input())
p=n*n
l=len(str(n))
s=0
for i in range(1,l+1):
    r=p%10
    s=s*10+r
    p=p//10
s1=0
for j in range(1,l+1):
    r1=s%10
    s1=s1*10+r1
    s=s//10
if n==s1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")