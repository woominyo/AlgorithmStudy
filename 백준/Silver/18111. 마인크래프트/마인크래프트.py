import sys
## 백준 18111
# M:가로 N:세로 B:인벤토리 블록 개수

# 집터 리스트
field = []

# 첫번째 줄
N, M, B = map(int, input().split())

# field 입력 받기
for row_num in range(N):
    field.append(list(map(int, input().split())))

# y_min = 256
# y_max = 0

# # feild 의 min과 max구하기
# for row in range(N):
#     for col in range(M):
#         if field[row][col] < y_min:
#             y_min = field[row][col]
        
#         if field[row][col] > y_max:
#             y_max = field[row][col]

best_time = 2*256*N*M # 최악의 시간 최소값으로 저장
best_y = 0

# range(y_min, y_max+1)동안 한번씩 걸리는 시간 구하기
for now_y in range(0, 257):
    now_time = 0
    now_B = B
    for this_N in field:
        for this_M in this_N:
            # 블록을 쌓아야 할 때
            temp = now_y - this_M
            if temp >  0:
                now_time += temp
                now_B -= temp

            # 블록을 파야 할 때
            elif temp < 0:
                now_time += 2 * abs(temp)
                now_B += -1 * temp
    
    # 인벤토리 개수가 음수면 무시
    if now_B < 0:
        continue

    # 방금 시간이 최소 시간일 때
    if now_time <= best_time:
        best_time = now_time
        best_y = now_y
        
print(best_time, best_y)
