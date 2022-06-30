n=int(input())
a=0
b=1
if n==0 or n==1:
    print(True)
else:
    c=0
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
            print(True)
    else:
            print(False)