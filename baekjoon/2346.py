### 문제 정보 ###
# 문제 번호: 2346
# 문제 이름: 풍선 터뜨리기
# 문제 링크: https://www.acmicpc.net/problem/2346

### 문제 풀이 ###
# 1. 1번 풍선 터뜨리기
# 2. j번 이동하면서 count하고, 풍선 속 숫자와 같아지면 해당 위치 풍선 터뜨리기
# 3. 모든 풍선이 터질 때까지 반복

# 풍선 개수 입력
n = int(input())

# 풍선 속 숫자 입력
numbers = list(map(int, input().split(" ")))

# 풍선 상태 리스트: 터지지 않았으면 1, 터졌으면 0
balloons = [1 for _ in range(n)]

# 1번 풍선 터뜨리고 시작
balloons[0] = 0
print(1, end=" ")

# 이후 연산
i = 0
while True:
    
    # 풍선이 모두 터졌으면 종료
    if sum(balloons) == 0:
        break
    
    # 그렇지 않으면 추가 연산
    else:
        j, count = i, 0
        
        while True:
            # 원형 구현
            if j >= len(balloons):
                j -= len(balloons)
            elif j < 0:
                j += len(balloons)
                
            count += balloons[j]
            if count == abs(numbers[i]):
                i = j
                print(i + 1, end=" ")
                balloons[i] = 0
                count = 0
                break
            else:
                if numbers[i] > 0:
                    j += 1
                elif numbers[i] < 0:
                    j -= 1