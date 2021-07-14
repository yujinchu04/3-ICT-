n=int(input())
b=[]
b.append(input().split())
d=sum(b, [])
#print(d)
dset=sorted(d);dset
dset.reverse()
c=[]
for j in d:
  c.append(dset.index(j)+1)
for i in range(len(c)):
  print(int(c[i]))

#15:9