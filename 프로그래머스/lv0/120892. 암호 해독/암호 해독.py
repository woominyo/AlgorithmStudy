def solution(cipher, code):
    answer = ''
    count = 1
    
    for char in cipher:
        if count % code == 0:
            answer += char
            count = 1
            continue
        count += 1
    
    return answer