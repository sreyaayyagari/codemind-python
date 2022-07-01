n=int(input())
l=list(map(int,input().split()))
even=0
for i in range(len(l)):
    if i%2==0:
        even=even+l[i]
print(even)                     