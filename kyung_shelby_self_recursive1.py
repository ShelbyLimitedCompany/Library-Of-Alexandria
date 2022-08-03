answer = ''


def dfs(x):
    global answer
    if x < 2:
        answer += str(x)

    else:
        dfs(x // 2)

        if x % 2:
            answer += '1'
        else:
            answer += '0'


if __name__ == '__main__':
    num = int(input())
    dfs(num)

    print(answer)