m,n=map(int,input().split())
max=0
for i in range(1,n):
    if m%i==0 and n%i==0:
        max=i
print(max)