memo = []
for i in range(100000):
    memo.append(0)
def star(n):
    if(not(memo[n])):
        if(n<=2):
            memo[n]=n
        else:
            memo[n] = star(n-1) + star(n-2)
    return memo[n]
n=int(input())
print(star(n))
#기말고사 문제
#20:12