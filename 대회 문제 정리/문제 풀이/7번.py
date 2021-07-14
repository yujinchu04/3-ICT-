n=int(input())
l=[]
c=0
d=0
for i in range(n):
    l.append(input().split())
for i in range(n):
    if int(l[i][0]) > int(l[i][1]):
        c+=int(l[i][1])
    if int(l[i][0]) < int(l[i][1]):
        d+=int(l[i][0])

print(c)
print(d)

#46:14