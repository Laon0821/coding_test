### 문제 정보 ###
# 문제 번호: 5073
# 문제 이름: 삼각형과 세 변
# 문제 링크: https://www.acmicpc.net/problem/5073

### 문제 풀이 ###
# 주어진 조건대로 수행
# 규칙의 우선순위는 판별하기 편한 순서대로

while True:
    
    a, b, c = map(int, input().split(" "))
    
    if (a == 0) & (b == 0) & (c == 0):
        break
    
    if max(a, b, c) >= ((a + b + c) - max(a, b, c)):
        print("Invalid")
        
    elif max(a, b, c) < ((a + b + c) - max(a, b, c)):
        if (a != b) & (b != c) & (c != a):
            print("Scalene")
        else:
            if (a == b) & (b == c) & (c == a):
                print("Equilateral")
            else:
                print("Isosceles")