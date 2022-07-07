n=int(input())
s=n*n
l=len(str(n))
a=0
for i in range(1,l+1):
    r=s%10
    a=a*10+r
    s=s//10
a=str(a)
a=a[::-1]
a=int(a)
if n==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")