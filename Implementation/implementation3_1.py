# 현재 나이트의 위치 입력받기
input_data = input()
col = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_col = col + step[1]
    next_row = row + step[0]
    if next_col >= 1 and next_row >= 1 and next_col <= 8 and next_row <= 8:
        result += 1

print(result)
