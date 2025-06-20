import heapq

def minimal_load_time(n, k, load_times, links, start, end):
    graph = [[] for _ in range(n)]
    for x, y in links:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    dist = [float('inf')] * n
    dist[start - 1] = 0
    heap = [(0, start - 1)]

    while heap:
        current_time, u = heapq.heappop(heap)
        if current_time > dist[u]:
            continue
        for v in graph[u]:
            new_time = current_time + load_times[v]
            if new_time < dist[v]:
                dist[v] = new_time
                heapq.heappush(heap, (new_time, v))

    result = dist[end - 1]
    return result + load_times[start - 1] if result != float('inf') else -1

def main():
    n, k = map(int, input().split())

    load_times = list(map(int, input().split()))

    links = [tuple(map(int, input().split())) for _ in range(k)]

    start, end = map(int, input().split())

    result = minimal_load_time(n, k, load_times, links, start, end)
    print(result)

if __name__ == "__main__":
    main()
