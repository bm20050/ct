# 08 문자열 재정렬

s = input()

result = []
sum = 0
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)
result.sort()
if sum != 0:
    result.append(str(sum))
result = "".join(result)

print(result)
