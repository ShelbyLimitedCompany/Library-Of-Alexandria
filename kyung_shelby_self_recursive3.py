"""

"""
# num = int(input())


import itertools

num, count = map(int, input().split())

temp = [range(1, num + 1)] * count

for tup in itertools.product(*temp):
    print(*tup)
