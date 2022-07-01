n=int(input())
l=list(map(int,input().split()))
even=0
odd=0
for i in range(len(l)):
    if i%2==0:
        even=even+l[i]
    elif i%2!=0:
        odd=odd+l[i]
print(abs(even-odd))   