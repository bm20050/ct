# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k # 가장 큰 수가 더해지는 횟수 {first, first, first,..., second} 수열 반복 횟수
count += m % (k + 1) # 수열 반복 후 나머지 first가 더해지는 횟수

result = 0
result += (count * first)
result += (m - count) * second

print(result)