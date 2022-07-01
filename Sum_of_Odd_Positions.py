n=int(input())
l=list(map(int,input().split()))
odd=0
for i in range(len(l)):
    if i%2!=0:
        odd=odd+l[i]
print(odd)          