# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
# 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

# 입력 시간은 24시간 표현을 사용한다. 
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 
# 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

# 분(m)을 -45 할 경우 00시에서 23시로 넘어가는 경우가 발생할 수 있음

h, m = map(int, input().split())

m -= 45
if m < 0:
    restMin = 60 + m
    m = restMin
    h -= 1
    if h < 0:
        h += 24
        
print(h, m)
