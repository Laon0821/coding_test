### 문제 정보 ###
# 문제 번호: 12789
# 문제 이름: 도키도키 간식드리미
# 문제 링크: https://www.acmicpc.net/problem/12789

### 문제 풀이 ###
# 1. 임시로 서 있을 공간을 tmp로 지정
# 2. 승환이가 간식을 먹을 수 있는 경우부터 생각: waits과 tmp 리스트의 길이가 모두 0
# 3. 각 리스트에 사람이 아무도 없는 경우 생각: waits 또는 tmp 리스트의 길이가 하나라도 0
## 리스트 특성 상 아무것도 없으면 비교 조차 안되기 때문
# 4. 양 리스트에 사람이 한 명이라도 서 있는 경우 생각: waits과 tmp 리스트의 길이가 모두 0이 아님
# 5. tmp의 가장 첫 번째 요소가 가장 작은 값이 아니면 승환이는 간식을 먹을 수 없음

# 입력
n = int(input())

# 현재 줄 서 있는 곳
waits = list(map(int, input().split(" ")))

# 한 명씩만 설 수 있는 공간
tmp = []

while True:
    
    # waits와 tmp에 아무도 없는 경우(=승환이가 간식을 받을 수 있는 경우)
    if (len(waits) == 0) & (len(tmp) == 0):
        print("Nice")
        break
    
    # waits에 아무도 없는 경우
    elif len(waits) == 0:
        # tmp의 맨 앞 사람이 가장 작은 숫자인 경우
        if tmp[0] == min(tmp):
            tmp.pop(0)
        # 그렇지 않은 경우
        else:
            print("Sad")
            break

    # tmp에 아무도 없는 경우
    elif len(tmp) == 0:
        # waits의 맨 앞 사람이 가장 작은 숫자인 경우
        if waits[0] == min(waits):
            waits.pop(0)
        # 그렇지 않은 경우
        else:
            tmp.insert(0, waits.pop(0))

    # 양쪽 다 사람이 있는 경우
    else:
        # tmp의 맨 앞 사람이 가장 작은 숫자인 경우
        if tmp[0] == min(waits + tmp):
            tmp.pop(0)
        # waits의 맨 앞 사람이 가장 작은 숫자인 경우
        elif waits[0] == min(waits + tmp):
            waits.pop(0)
        # waits의 맨 앞 사람이 가장 작은 숫자가 아닌 경우
        elif waits[0] != min(waits + tmp):
            tmp.insert(0, waits.pop(0))
        # 그렇지 않은 경우
        else:
            print("Sad")
            break