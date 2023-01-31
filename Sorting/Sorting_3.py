# 두 배열의 원소 교체

n, k = map(int, input().split()) # n과 k를 입력받기
a = list(map(int, input().split())) # 배열 a의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 b의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
