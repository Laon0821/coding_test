### 문제 정보 ###
# 문제 번호: 10815
# 문제 이름: 숫자 카드
# 문제 링크: https://www.acmicpc.net/problem/10815

### 문제 풀이 ###
# 

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split(" ")))

start, end = 0, n

def binary_search(start: int, end: int, num: int) -> int:
    
    if len(n_list) == 0:
        return 0
    else:
        hp = (end - start) // 2
        if n_list[hp] == num:
            return 1
        else:
            if n_list[hp] < num:
                start = hp + 1
                return binary_search(start, end, num)
            else:
                end = hp
                binary_search(start, end, num)

n_list.sort()

for i in range(m):
    print(binary_search(start, end, m_list[i]), end=" ")