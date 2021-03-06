# Dynamic Programming
# p.228

# 화폐 종류의 개수 n, 값의 합 m 을 입력받음
n, m = map(int, input().split())

# 화폐 종류 n개를 입력받음
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (Bottom-Up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재할 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
            
if d[m] == 10001: # m원을 만들 방법이 없는 경우
    print(-1)
else:
    print(d[m])
