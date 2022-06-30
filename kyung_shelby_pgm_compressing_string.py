"""
데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.
예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.
"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면
"2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만,
3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때,
위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.


21:20 ~ 21:50 : 문제풀이
21:50 ~ 22:20: 답지 보고 다시 풀기


==== solution ====
1. 문자열을 쪼갤 단위를 나타내는 count 가 2부터 string 의 길이까지, 다음 과정을 반복한다.
    1). 문자열을 count 단위로 쪼갠 값들을 원소로 갖는 리스트를 생성한다.
    2). 해당 리스트를 순회하면서, 다음 과정을 반복한다.
        2.1) 마지막 n 이 마지막 원소인 경우,
            - 현재까지의 출현 빈도가 1 이상이면
                빈도 + 해당 문자 를 결과 문자열에 더한다.
            - 현재까지의 출현 빈도가 1 이면
                해당 문자를 결과 문자열에 더한다.

        2.2) n 번째 원소와 n + 1 번째 원소의 값이 같으면,
            출현 빈도 값를 +1 한다.

        2.3) n 번째 원소와 n + 1 번째 원소의 값이 다르면,
            현재 출현 빈도 값이 1보다 크면,
                결과 문자열에 해당빈도 수 + n번째 원소 값 을 결과 문자열에 더한다.
                출현 빈도를 1로 초기화한다.

            현재 출현 빈도 값이 1이면
                결과 문자열에 n번째 원소 값 을 결과 문자열에 더한다.


    3). 마지막 count 까지 1)~3) 과정을 수행한 뒤, 가장 작은 값을 정답으로 리턴한다.
"""


def slice_by_count(num, string):
    print(f"num: {num}, string: {string}")
    sliced_string = []
    answer_candidate = ''
    continue_count = 1

    for i in range(0, len(string), num):
        sub_string = string[i:i+num]
        sliced_string.append(sub_string)

    print(sliced_string)

    for i in range(len(sliced_string)):
        if i == len(sliced_string) - 1:
            print("마지막 원소")
            if continue_count > 1:
                answer_candidate += str(continue_count) + sliced_string[i]
            else:
                answer_candidate += sliced_string[i]

            break

        if sliced_string[i] == sliced_string[i+1]:
            continue_count += 1
            print(f"{i} 번쨰와 {i+1} 원소 같음, continue_count = {continue_count}")
        else:
            if continue_count > 1:
                answer_candidate += str(continue_count) + sliced_string[i]
                continue_count = 1

            else:
                answer_candidate += sliced_string[i]
            print(f"{i} 번쨰와 {i+1} 원소 다름, continue_count = {continue_count}, answer_candidate: {answer_candidate}")

    print(f"최종 string: {answer_candidate}")
    return len(answer_candidate)


def solution(input_string):
    answer = len(input_string)

    if len(input_string) == 1:
        return 1

    for i in range(1, len(input_string) // 2 + 1):
        temp = slice_by_count(i, input_string)
        print(f"temp: {temp}")
        print()

        if answer > temp:
            answer = temp

    return answer


if __name__ == '__main__':
    s = [
        "aabbaccc",
        "ababcdcdababcdcd",
        "abcabcdede",
        "abcabcabcabcdededededede",
        "xababcdcdababcdcd"
    ]

    answers = [7, 9, 8, 14, 17]

    for i in range(len(s)):
        print(f"{i+1 } case answer: {solution(s[i])}")