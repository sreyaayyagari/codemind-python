n=int(input())
l=len(str(n))
c=0
for i in range(1,l+1):
    r=n%10
    n=n//10
    c+=1
if c==10 and l==10:
    print("Valid")
else:
    print("Invalid")
