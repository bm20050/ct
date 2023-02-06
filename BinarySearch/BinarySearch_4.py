# 떡볶이 떡 만들기

def binary_search(array, m, start, end):
    while (start <= end):
        mid = (start + end) // 2
        length = 0
        for a in array:
            if a > mid:
                length += a - mid
        if length == m:
            return mid
        elif length > m:
            start = mid + 1
        else:
            end = mid - 1
    return -1

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

maxValue = max(array)
minValue = min(array)

print(binary_search(array, m, 0, maxValue))