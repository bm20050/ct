# 07 럭키 스트레이트

n = int(input())
s = str(n)
sum1 = 0
sum2 = 0
x = len(s) // 2
for i in range(x):
    sum1 += int(s[i])
for i in range(x, len(s)):
    sum2 += int(s[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
