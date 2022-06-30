a=int(input())
for j in range(1,a+1):
    m,n=map(int,input().split( ))
    for i in range(0,n+1):
        if (i*i)%n==m:
            print(i)
            break
    else:
        print("-1")