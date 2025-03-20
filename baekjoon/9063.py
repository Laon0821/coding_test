### 문제 정보 ###
# 문제 번호: 9063
# 문제 이름: 대지
# 문제 링크: https://www.acmicpc.net/problem/9063

### 문제 풀이 ###
# 결국 옥구슬이 나오는 x좌표와 y좌표의 최대값 - 최소값을 구하면 됨

n = int(input())

x_points, y_points = [], []
for _ in range(n):
    x_point, y_point = map(int, input().split(" "))
    
    x_points.append(x_point)
    y_points.append(y_point)
    
x_min = min(x_points)
x_max = max(x_points)
y_min = min(y_points)
y_max = max(y_points)

area = (x_max - x_min) * (y_max - y_min)

print(area)