#시간 제한인 1초 넘음 ~ runtime error
n=int(input())
def Prime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

lis=[]
for i in range(n+1):
  if(Prime(i)):
    lis.append(i)

for i in range(len(lis)):
    while n%lis[i]==0:
        print(lis[i],end=" ")
        n=n//lis[i]
#42:38