# 17 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def f(num):
    for i in range(n):
        for j in range(n):
            if data[i][j] == num:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if data[nx][ny] == 0:
                            data[nx][ny] = num

for _ in range(s):
    for i in range(1, k + 1):
        f(i)

print(data[x][y])