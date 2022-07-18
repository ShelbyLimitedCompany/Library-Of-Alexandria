# row_count, max_virus = map(int, input().split())
# board = []
# for _ in range(row_count):
#     board.append(list((map(int, input().split()))))
# seconds, target_x, target_y = map(int, input().split())

row_count, max_virus = 3, 3
board = [[1, 0, 2], [0, 0, 0], [2, 3, 2]]
seconds, target_x, target_y = 2, 3, 2


d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]


def dfs(x, y, virus_priority):
    """
    원소 값이 0 이상, x, y 값이 정상인 곳에 대해서, virus_priority 를 가지고 전염을 시키는 재귀함수
    :param x:
    :param y:
    :param virus_priority:
    :return:
    """
    print(f"dfs: row: {row}, col: {col}, board: {board[row][col]}")

    if virus_priority == 0:
        return

    if virus_priority < board[x][y]:
        board[x][y] = virus_priority

    for i in range(4):
        new_row = row + d_row[i]
        new_col = col + d_col[i]

        if 0 <= new_row < row_count and \
                0 <= new_col < row_count and \
                0 < board[new_row][new_col]:
            dfs(new_row, new_col, board[row][col])

    return


if __name__ == '__main__':
    # 10,000 * 200 * 200 * 4
    for _ in range(seconds):
        for row in range(row_count):
            for col in range(row_count):
                print("main")
                dfs(row, col, board[row][col])

    print(board[target_x][target_y])
