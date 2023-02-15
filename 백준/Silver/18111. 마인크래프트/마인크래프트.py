## 백준 18111
# M:가로 N:세로 B:인벤토리 블록 개수
import sys
# 집터 리스트
field = []

# 첫번째 줄
N, M, B = map(int, sys.stdin.readline().split())

# field 입력 받기
for row_num in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))

y_min = min(map(min, field))
y_max = max(map(max, field))


best_time = 2 * 256 * N * M  # 최악의 시간 최소값으로 저장
best_y = 0

# range(y_min, y_max+1)동안 한번씩 걸리는 시간 구하기
# 반복문 돌릴때 인덱스로 접근 하는 것보다 요소로 하는게 빠름 <- 이거 때문에 계속 시간초과
for now_y in range(y_min, y_max + 1):
    now_time = 0
    now_B = B
    for row in field:
        for col in row:
            difference = now_y - col  # 목표로하는 블록의 높이와 현재 높이의 차이
            # 블록을 쌓아야 할 때
            if difference > 0:
                now_time += difference
                now_B -= difference

            # 블록을 파야 할 때
            elif difference < 0:
                now_time += 2 * abs(difference)
                now_B += -1 * difference

    # 인벤토리 개수가 음수면 무시
    if now_B < 0:
        continue

    # 방금 시간이 최소 시간일 때
    if now_time <= best_time:
        best_time = now_time
        best_y = now_y

print(best_time, best_y)
