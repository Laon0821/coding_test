### 문제 정보 ###
# 문제 번호: 14215
# 문제 이름: 세 막대
# 문제 링크: https://www.acmicpc.net/problem/14215

### 문제 풀이 ###
# 삼각형이 이루어지는 조건: 가장 긴 변이 남은 두 변의 합보다 작음
# 따라서 크기를 정렬할 수 있는 리스트 사용

lengths = list(map(int, input().split(" ")))

lengths.sort()

if lengths[-1] < lengths[0] + lengths[1]:
    print(sum(lengths))
else:
    lengths[-1] = lengths[0] + lengths[1] - 1
    print(sum(lengths))