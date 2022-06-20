"""
BOJ 18532, https://www.acmicpc.net/problem/18352
어떤 나라에는 1번부터 N 번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
이 때 특정한 도시 X 로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

BFS 풀이. Python3 으로 제출하면 시간 초과가 나고, pypy3 으로 제출해야 한다.
"""
from collections import deque

city_count, load_count, target_distance, initial_start_city = map(int, input().split())

graph = [[] for i in range(city_count+1)]

for _ in range(load_count):
    source, destination = map(int, input().split())
    graph[source].append(destination)

visited = [False] * (city_count + 1)

distances = [0] * (city_count + 1)
answer = []

if __name__ == '__main__':
    visited[initial_start_city] = True
    queue = deque([initial_start_city])

    while queue:
        start = queue.popleft()

        for city in graph[start]:
            if visited[city] is False:
                visited[city] = True
                distances[city] += distances[start] + 1
                queue.append(city)

    check = False
    for i in range(1, city_count + 1):
        if distances[i] == target_distance:
            print(i)
            check = True

    # 만약 최단 거리가 K인 도시가 없다면, -1 출력
    if check == False:
        print(-1)


