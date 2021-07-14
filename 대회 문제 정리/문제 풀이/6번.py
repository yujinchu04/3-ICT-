n=int(input())
count=1
while n!=1:
    if n%2==0:
        n=n/2
        count+=1
    elif n%2!=0:
        n=3*n+1
        count+=1
print(count)
#39:14