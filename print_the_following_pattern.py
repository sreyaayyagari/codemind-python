n=int(input())
i=1
j=1
for i in range(1,n+1):
    for j in range (1,n+2-i):
        print(j, end="")
    print()        