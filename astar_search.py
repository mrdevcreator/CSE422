import heapq

def read_data(file_name):
    graph = {}
    heuristics = {}
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split()
            node = data[0]
            heuristics[node] = int(data[1])
            neighbors = {}
            for i in range(2, len(data), 2):
                neighbor = data[i]
                distance = int(data[i + 1])
                neighbors[neighbor] = distance
            graph[node] = neighbors
    return graph, heuristics

def astar_search(graph, heuristics, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for neighbor, distance in graph[current].items():
            tentative_g_score = g_score[current] + distance
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path


graph, heuristics = read_data('Input file.txt')

start = input("Start: ")
destination = input("Destination: ")


path = astar_search(graph, heuristics, start, destination)
if path:
  print("Path:", " => ".join(path))
  distance = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
  print("Total distance:", distance, "km")
else:
  print("NO PATH FOUND")

