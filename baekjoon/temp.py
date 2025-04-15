### 문제 정보 ###
# 문제 번호: 1339
# 문제 이름: 단어 수학
# 문제 링크: https://www.acmicpc.net/problem/1339

### 문제 풀이 ###
# 1. scores 딕셔너리를 생성해서 각 알파벳 별 점수 저장
# 2. 점수는 각 알파벳의 가장 큰 자리 수를 계산: 단어의 길이 - 단어 내 알파벳의 인덱스
# 3. 점수에 따라 scores 정렬 후, 9부터 0까지 value 변경
# 4. scores의 Key(알파벳)와 Value(숫자)를 기반으로 mapping하여 합계 반환

import sys

n = int(sys.stdin.readline())

flowers = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))

    start = tmp[0:2]
    end = tmp[2:4]

    flowers.append([start, end])

flowers.sort(key=lambda x: x[1][0] - x[0][0], reverse=True)

month = [0 for _ in range(12)]
for flower in flowers:
    
    if sum(month) >= 12:
        break
    
    else:
        month[flower[0][0]:flower[1][0]] = [1 * flower[1][0] - flower[0][0]]


print(flowers)
print(month)