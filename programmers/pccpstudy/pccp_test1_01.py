def solution(input_string):
    answer = ''
    used = [] #한번이라도 나온 알파벳
    loner = []
    before_char = ''
    #
    for char in input_string:
        if char == before_char:
            continue

        if char not in used:
            used.append(char)
        elif char in used:
            loner.append(char)

        before_char = char
    loner = list(set(loner))
    loner.sort()
    answer = ''.join(loner)
    if answer == '':
        return 'N'

    return answer


# "de"
print(solution("edeaaabbccd"))
