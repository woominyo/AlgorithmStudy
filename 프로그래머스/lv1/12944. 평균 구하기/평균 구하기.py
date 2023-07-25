def solution(arr):
    count = 0
    sum_arr = 0
    
    for i in arr:
        sum_arr += i
        count += 1
    return sum_arr / count