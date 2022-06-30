n=int(input())
a=n
sum=0
while n:
    i=1
    fact=1
    r=n%10
    while i<=r:
        fact=fact*i
        i+=1
    sum=fact+sum
    n=n//10
if a==sum:
    print("The number" ,a, "is a strong number")
else:
    print("The number" ,a, "is not a strong number")