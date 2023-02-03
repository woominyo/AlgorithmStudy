S = input()
K = input()

no_num_S = []
# S를 돌면서 숫자는 거르고 문자만 no_num_S에 추가
for s in range(len(S)):
    if S[s].isalpha():
        no_num_S.append(S[s])


for s_check in range(len(no_num_S)):
    if no_num_S[s_check] == K[0]:
        is_K_in = 0
        for k_check in range(len(K)):
            if no_num_S[s_check+k_check] == K[k_check]:
                is_K_in = 1
            else:
                is_K_in = 0
                break
            if k_check == len(K)-1 and is_K_in == 1:
                print(is_K_in)
                exit()

print(is_K_in)
