n=int(input())
c=0
for i in range(1,n//2+1):
    if i*i==n and n//i==i:
        c+=1
if c>0:
    print(True)
else:
    print(False)