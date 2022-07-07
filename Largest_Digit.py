n=int(input())
a=0
for i in range(len(str(n))):
    r=n%10
    if r>a:
        a=r
    n=n//10
print(a)        
       