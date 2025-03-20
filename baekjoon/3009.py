### 문제 정보 ###
# 문제 번호: 3009
# 문제 이름: 네 번째 점
# 문제 링크: https://www.acmicpc.net/problem/3009

### 문제 풀이 ###
# 1. x와 y를 각각 입력 받아서 각각 원소의 개수가 2개가 아닌 값 반환

x_points, y_points = [], []
for _ in range(3):
    x_point, y_point = map(int, input().split(" "))
    
    x_points.append(x_point)
    y_points.append(y_point)
    
result = []
for i in range(len(x_points)):
    if x_points.count(x_points[i]) != 2:
        result.append(x_points[i])
    else:
        continue
for i in range(len(y_points)):
    if y_points.count(y_points[i]) != 2:
        result.append(y_points[i])
    else:
        continue
    
print(" ".join(map(str, result)))