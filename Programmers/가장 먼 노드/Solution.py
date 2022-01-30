from collections import deque, defaultdict


def solution(n, vertex):
    graph = vertexToGraph(vertex)
    distance = [0] * n
    visited = []
    queue = deque([1])
    while queue:
        currentNode = queue.popleft()
        for nextNode in graph[currentNode]:
            if (nextNode not in visited) and (nextNode not in queue):
                queue.append(nextNode)
                distance[nextNode-1]=distance[currentNode-1]+1
        visited.append(currentNode)
    return distance.count(max(distance))


def vertexToGraph(vertex):
    graph = defaultdict(set)
    for i in vertex:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])
    return graph