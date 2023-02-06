# 부품 찾기

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

# n(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
narray = list(map(int, input().split()))
# m(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
marray = list(map(int, input().split()))

narray.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in marray:
    if binary_search(narray, i, 0, n - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
