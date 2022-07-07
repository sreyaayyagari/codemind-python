n=input()
s=''
for i in n:
    if i not in s:
        s+=i
if len(s)==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")