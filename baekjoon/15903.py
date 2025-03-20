### 문제 정보 ###
# 문제 번호: 15903
# 문제 이름: 카드 합체 놀이
# 문제 링크: https://www.acmicpc.net/problem/15903

### 문제 풀이 ###
# 1. cards 리스트 정렬
# 2. 가장 작은 수와 그 다음으로 작은 수를 두 수의 합으로 변경
# 3. m번 반복 후, cards 리스트의 합계 반환

n, m = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

count = 0
while count < m:
    
    cards.sort()
    
    cards[0], cards[1] = cards[0] + cards[1], cards[0] + cards[1]

    count += 1    

print(sum(cards))