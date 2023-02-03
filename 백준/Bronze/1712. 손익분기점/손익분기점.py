A, B, C = map(int, input().split())

if B >= C:
    print(-1)
    exit()

print(A // (C-B)+1)
