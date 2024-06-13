import Stack_Queue_LinkedList as queue

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

def breadth_first_search(graph, start_vertex, distances=dict()):
    discovered_set = set()
    frontier_queue = queue.Queue()
    visited_list = []
    distances[start_vertex] = 0
    frontier_queue.enqueue(start_vertex)
    discovered_set.add(start_vertex)
    while (frontier_queue.list.head != None):
        current_vertex = frontier_queue.dequeue()
        visited_list.append(current_vertex)
        for adjacent_vertex in graph.adjacency_list[current_vertex]:
            if adjacent_vertex not in discovered_set:
                frontier_queue.enqueue(adjacent_vertex)
                discovered_set.add(adjacent_vertex)
                distances[adjacent_vertex] = distances[current_vertex] + 1
    return visited_list

def depth_first_search(graph, start_vertex, visit_function):
    vertex_stack = [start_vertex]
    visited_set = set()
    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        if current_vertex not in visited_set:
            visit_function(current_vertex)
            visited_set.add(current_vertex)
            for adjacent_vertex in graph.adjacency_list[current_vertex]:
                vertex_stack.append(adjacent_vertex)

def dijkstra_shortest_path(graph, start_vertex):
    unvisited_queue = []
    for current_vertex in graph.adjacency_list:
        unvisited_queue.append(current_vertex)
    start_vertex.distance = 0
    while len(unvisited_queue) > 0:
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        for adj_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

def get_shortest_path(start_vertex, end_vertex):
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = '->' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path