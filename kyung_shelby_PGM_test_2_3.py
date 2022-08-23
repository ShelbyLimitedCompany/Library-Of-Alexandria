from collections import deque


def solution(n, roads, sources, destination):
    graph = {}
    answer = []

    for i in range(1, n + 1):
        graph[i] = []

    for src, dest in roads:
        graph[src].append(dest)
        graph[dest].append(src)

    for start in sources:
        if start == destination:
            answer.append(0)
            continue

        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        distance = [0] * (n + 1)

        flag = False
        while queue:
            src = queue.popleft()

            for dest in graph[src]:
                if not visited[dest]:
                    queue.append(dest)
                    visited[dest] = True
                    distance[dest] = distance[src] + 1

                    if dest == destination:
                        answer.append(distance[dest])
                        flag = True
                        break
            if flag:
                break

        if distance[destination] == 0:
            answer.append(-1)

    return answer

