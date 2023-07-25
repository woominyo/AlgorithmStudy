paper_num = int(input())
black_papers = []

# 검은색 색종이 리스트
for paper in range(paper_num):
    black_papers.append(list(map(int, input().split())))

# 배경 흰종이 리스트 만들기
bg_paper = [[0 for _ in range(100)] for _ in range(100)]

# 검은색 색종이 부분은 1씩 더해준다
for black_papers in black_papers:
    end_point = [black_papers[0] + 10, black_papers[1] + 10]
    for row in range(black_papers[0], end_point[0]):
        for col in range(black_papers[1], end_point[1]):
            bg_paper[row][col] += 1

# 넓이 구하기
count_area = 0
for row in bg_paper:
    for col in row:
        if col == 0:
            continue
        count_area += 1

print(count_area)


