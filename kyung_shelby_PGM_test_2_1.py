import itertools


def solution(number):
    answer = 0

    for a, b, c in itertools.combinations(number, 3):
        if a + b + c == 0:
            answer += 1

    return answer
