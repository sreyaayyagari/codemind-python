n=int(input())
l=list(map(int,input().split()))
even=0
odd=0
for i in l:
    if i%2==0:
        even=even+i
    elif i%2!=0:
        odd=odd+i
print(abs(even-odd))   