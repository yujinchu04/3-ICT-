n=list(input().split())
a=int(n[0])
b=int(n[1])
def Prime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

lis=[]
for i in range(a,b+1):
  if(Prime(i)):
    lis.append(i)

print(len(lis))
print(max(lis)) #Runtime Error!
#12:32