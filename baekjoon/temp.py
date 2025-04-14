### 문제 정보 ###
# 문제 번호: 1781
# 문제 이름: 컵라면
# 문제 링크: https://www.acmicpc.net/problem/1781

### 문제 풀이 ###
# 1. 같은 데드라인인 경우, 컵라면을 많이 주는 문제를 선택
# 2. 다음의 우선순위를 기준으로 정렬: (1)데드라인, (2)컵라면
# 3. 리스트를 딕셔너리로 변경
## * 딕셔너리에 Key가 존재할 경우, 늦게 입력된 Value로 대체
## * = 각 데드라인별 최대 컵라면 개수
# 4. 딕셔너리 Value의 합계 출력

import sys

n = int(sys.stdin.readline())

problems = []
for _ in range(n):
    problems.append(list(map(int, sys.stdin.readline().split(" "))))

def cupRamen(li: list) -> int:
    
    li.sort(key=lambda x: (x[0], x[1]))
    result = [0 for _ in range(li[-1][0])]
    
    for i in range(len(result)):
        


problems.sort(key=lambda x: (x[0], x[1]))


print(problems)