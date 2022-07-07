n=int(input())
a=0
b=1
c=0
s=0
while c<=n:
    c=a+b
    if c==n:
        s+=1
    a=b
    b=c
if s>0:
    print(True)
else:
    print(False)