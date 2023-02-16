# 12 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    array = [[2] * (n + 1) for _ in range(n + 1)]
    answer = []
    for i in build_frame:
        a, b = i[0], i[1]
        if i[3] == 1:
            array[a][b] = i[2]
        else:
            array[a][b] = 2
    for i in range(1, n + 1):
        for j in range(n):
            if array[i][j] != 2:
                answer.append([i, j, array[i][j]])

    return answer



n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))
print(solution(n, build_frame2))