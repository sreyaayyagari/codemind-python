N=int(input())
temp=N
sum=0
d=0
while temp>0:
    d=temp%10
    sum=sum+d
    temp=temp//10
if N%sum==0:
    print('True')
else:
    print('False')