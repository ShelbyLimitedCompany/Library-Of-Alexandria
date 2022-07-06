"""
https://school.programmers.co.kr/learn/courses/30/lessons/92334

문제 설명
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

유저 ID	        유저가 신고한 ID	    설명
"muzi"	        "frodo"	            "muzi"가 "frodo"를 신고했습니다.
"apeach"	    "frodo"	            "apeach"가 "frodo"를 신고했습니다.
"frodo"	        "neo"	            "frodo"가 "neo"를 신고했습니다.
"muzi"	        "neo"	            "muzi"가 "neo"를 신고했습니다.
"apeach"	    "muzi"	            "apeach"가 "muzi"를 신고했습니다.
각 유저별로 신고당한 횟수는 다음과 같습니다.

유저 ID	신고당한 횟수
"muzi"	1
"frodo"	2
"apeach"	0
"neo"	2
위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다.
이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

유저 ID	        유저가 신고한 ID	    정지된 ID
"muzi"	        ["frodo", "neo"]	["frodo", "neo"]
"frodo"	        ["neo"]	            ["neo"]
"apeach"	    ["muzi", "frodo"]	["frodo"]
"neo"	        없음	없음
따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 ID가 담긴 문자열 배열 id_list,
각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report,
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때,
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
    2 ≤ id_list 의 길이 ≤ 1,000
    1 ≤ id_list 의 원소 길이 ≤ 10
    id_list 의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    id_list 에는 같은 아이디가 중복해서 들어있지 않습니다.
    1 ≤ report 의 길이 ≤ 200,000
    3 ≤ report 의 원소 길이 ≤ 21
    report 의 원소는 "이용자 id 신고한 id"형태의 문자열입니다.
    예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    id는 알파벳 소문자로만 이루어져 있습니다.
    이용자 id 와 신고한 id 는 공백(스페이스)하나로 구분되어 있습니다.
    자기 자신을 신고하는 경우는 없습니다.
    1 ≤ k ≤ 200, k는 자연수입니다.
    return 하는 배열은 id_list 에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.
입출력 예
id_list	report	k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]
입출력 예 설명
입출력 예 #1

문제의 예시와 같습니다.

입출력 예 #2
"ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리합니다.
따라서 "con"은 1회 신고당했습니다.
3번 이상 신고당한 이용자는 없으며, "con"과 "ryan"은 결과 메일을 받지 않습니다. 따라서 [0, 0]을 return 합니다.


============SOLUTION============
1차 시도
- 그래프 자료구조에서 node 를 흉내낸 객체를 만들어서 풀이하려고 했다.
- 접근 자체는 정답과 크게 벗어나지 않았으나, 특정 user 를 조회하는데 배열의 모든 우너소를 순회하는 등 비효율이 많았다.
- 또한, report 의 중복 제거를 고려하지 않았다.
- 시간 초과가 났다.

2차 시도
- set 을 이용해 report 의 중복을 제거했다.
- 불필요하게 list 로 바꾸는 부분들(예를 들면 list(dictionary.keys()) 같은 부분들을 제거했다.
- 3개의 케이스에서 시간 초과가 났다.

3차 시도
- report 를 순회하면서, user 를 순회한다는 점이 시간 초과가 날 것 같았다. (200000 * 1000 * {k 회 이상 신고당한 user 를 신고한 user 수})
- 2중 for 문을 아예 없애고, 가능한 한 모든 것을 dictionary 로 조회하면 2중 for 문을 돌릴 이유가 없을 것 같았다.
- 각 사용자의 이름을 key 로 갖고, value 로는 해당 사용자를 신고한 사용자 배열, 해당 사용자가 신고한 사용자 배열, 알림 받은 수 를 각각 key-value
    를 형태로 저장하는 딕셔너리를 갖게 했다.

    "kks": {
        "in": [],
        "out": [],
        "count": 0
    }

- 그러자 report 를 순회하는 것 만으로 정답을 구할 수 있는 데이터가 완성되었다.
- 이 report 에서, 사용자 id 를 통해 "in" 에 접근하여, count 가 k 이상인 user 를 신고한 사용자에의 count 를 증가시켰다.
- 정답이었다.

"""
from collections import defaultdict
from typing import List


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.in_user = defaultdict()
#         self.out_user = defaultdict()
#         self.notified_count = 0
#
#     def __repr__(self):
#         return f"username: {self.name}, in: {self.in_user}, out: {self.out_user}, notified_count: {self.notified_count}\n"


def solution_try_1(id_list: List, report: List[str], k: int):
    answer = []

    # 1000
    users = [User(user_id) for user_id in id_list]
    notified_count_dict = defaultdict()

    report = set(report)

    # 200000
    for r in report:
        src, trg = r.split()

        # 1000
        for u in users:
            notified_count_dict[u.name] = 0

            if u.name == src:
                u.out_user[trg] = 1

            if u.name == trg:
                u.in_user[src] = 1

    # 1000
    for u in users:
        if len(u.in_user.keys()) >= k:

            for in_user_name in u.in_user.keys():
                notified_count_dict[in_user_name] += 1

    for _, v in notified_count_dict.items():
        answer.append(v)

    return answer


class User:
    def __init__(self, name):
        self.name = name
        self.in_user = []
        self.out_user = []
        self.notified_count = 0

    def __repr__(self):
        return f"username: {self.name}, in: {self.in_user}, out: {self.out_user}, notified_count: {self.notified_count}\n"


def solution_try_2(id_list: List, report: List[str], k: int):
    answer = []

    users = [User(user_id) for user_id in id_list]
    notified_count_dict = defaultdict()

    report = set(report)

    for r in report:
        src, trg = r.split()

        # 1000
        for u in users:
            notified_count_dict[u.name] = 0

            if u.name == src:
                u.out_user.append(trg)

            if u.name == trg:
                u.in_user.append(src)

    for u in users:
        if len(u.in_user) >= k:
            for in_user_name in u.in_user:
                notified_count_dict[in_user_name] += 1

    for _, v in notified_count_dict.items():
        answer.append(v)

    return answer


def solution(id_list: List, report: List[str], k: int):
    length = len(id_list)

    table = {}
    report = set(report)

    for id_ in id_list:
        table[id_] = {
            "in": [],
            "out": [],
            "notified_count": 0
        }

    for r in report:
        src, trg = r.split()

        table[src]["out"].append(trg)
        table[trg]["in"].append(src)

    for key, value in table.items():
        if len(table[key]["in"]) >= k:
            for in_user in table[key]["in"]:
                table[in_user]["notified_count"] += 1

    answer = [value["notified_count"] for _, value in table.items()]
    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"]
    k = 2

    assert [2, 1, 1, 0] == solution(id_list, report, k)


    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3

    assert [0, 0] == solution(id_list, report, k)
