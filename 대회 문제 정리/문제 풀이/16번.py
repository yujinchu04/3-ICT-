a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
li=[a,b,c]
li.sort()
if li[0]+li[1] <= li[2]:
    print(0)
elif li[0]==li[1] and li[1]==li[2]:
    print(1)
elif li[0]==li[1] or li[1]==li[2]:
    print(2)
elif li[0]**2 + li[1]**2 == li[2]**2:
    print(3)
else: print(4)
#31:54