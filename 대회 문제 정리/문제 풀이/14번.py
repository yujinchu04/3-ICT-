n=int(input())
dp=[-1 for i in range(1000)]
#print(dp)

def fibo1(n):
    if n==1: return 1
    if n==2: return 1
    if dp[n]!=-1: return dp[n]
    dp[n] = fibo1(n-1) + fibo1(n-2)
    return dp[n]

print(fibo1(n))
#메모이제이션 사용
#48:26