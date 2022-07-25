from collections import deque


row_count, max_virus = map(int, input().split())
board = []
data = []

for i in range(row_count):
    board.append(list(map(int, input().split())))

    for j in range(row_count):
        if board[i][j] != 0:
            data.append([board[i][j], 0, i, j])

data.sort()
queue = deque(data)

seconds, target_x, target_y = map(int, input().split())

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]


if __name__ == '__main__':
    while queue:
        virus_priority, time, x, y = queue.popleft()

        # 시간이 초과한 경우
        if time == seconds:
            break

        for i in range(4):
            new_x = x + d_row[i]
            new_y = y + d_col[i]

            if 0 <= new_x < row_count and 0 <= new_y < row_count:
                if board[new_x][new_y] == 0:
                    board[new_x][new_y] = virus_priority
                    queue.append([virus_priority, time + 1, new_x, new_y])

    print(board[target_x - 1][target_y - 1])
