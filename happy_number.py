N=int(input())
sum=0
while sum!=1 and sum!=4:
    sum=0
    while N>0:
        d=N%10
        sum=sum+(d*d)
        N=N//10
    N=sum
if sum==1:
    print('True')
else:
    print('False')