def binary_search(array, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if ()

n, m = map(int, input().split())
array = list(map(int, input().split()))

maxValue = max(array)
minValue = min(array)

print(binary_search(array, minValue, maxValue))