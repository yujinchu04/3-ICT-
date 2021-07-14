n=list(input().split())
n.sort()
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=0
for i in range(1,a+1):
    if a%i==0:
        if b%i==0:
            if c%i==0:
                d=i

print(d)
#44:30