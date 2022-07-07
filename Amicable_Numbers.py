m=int(input())
n=int(input())
a=0
b=0
for i in range(1,n//2+1):
    if n%i==0:
        a=a+i
for j in range(1,m//2+1):
    if m%j==0:
        b=b+j
if a==m and b==n:
    print("Amicable")
else:
    print("Not Amicable")