coin_type_num, sum_value = map(int, input().split())
coin_types = []
for _ in range(coin_type_num):
    coin_types.append(int(input()))

coin_types.reverse()
type_count = 0
coin_count = 0
while sum_value != 0:
    if sum_value < coin_types[type_count]:
        type_count += 1
    else:
        sum_value -= coin_types[type_count]
        coin_count += 1
    
print(coin_count)