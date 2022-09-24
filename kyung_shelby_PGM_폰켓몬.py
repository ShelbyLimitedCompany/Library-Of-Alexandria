"""
문제 링크
https://school.programmers.co.kr/learn/courses/30/lessons/1845

문제좀 쉽게 써놔라...
"""

def solution(nums):
    monster_table = {}
    target_num = len(nums) // 2

    for num in nums:
        monster_table.setdefault(num, 0)
        monster_table[num] += 1

    type_cnt = len(monster_table)

    if target_num < type_cnt:
        return target_num

    return type_cnt