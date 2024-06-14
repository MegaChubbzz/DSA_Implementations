import Stack_Queue_LinkedList as queue

class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = 1
        self.pred_vertex = None

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

    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None
    
    def get_vertex_list(self):
        return list(self.adjacency_list)
    
    def get_incoming_edges(self, vertex):
        incoming = []
        for edge in self.edge_weights:
            if edge[1] is vertex:
                incoming.append(edge)
        return incoming

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

def bellman_ford(graph, start_vertex):
    for current_vertex in graph.adjacency_list:
        current_vertex.distance = float('inf')
        current_vertex.pred_vertex = None
    start_vertex.distance = 0
    for i in range(len(graph.adjacency_list) - 1):
        for current_vertex in graph.adjacency_list:
            for adj_vertex in graph.adjacency_list[current_vertex]:
                edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight
                if alternative_path_distance < adj_vertex.distance:
                    adj_vertex.distance = alternative_path_distance
                    adj_vertex.pred_vertex = current_vertex
    for current_vertex in graph.adjacency_list:
        for adj_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight
            if alternative_path_distance < adj_vertex.distance:
                return False
    return True

def get_incoming_edge_count(edge_list, vertex):
    count = 0
    for (from_vertex, to_vertex) in edge_list:
        if to_vertex is vertex:
            count = count + 1
    return count

def topological_sort(graph):
    result_list = []
    no_incoming = []
    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            no_incoming.append(vertex)
    remaining_edges = set(graph.edge_weights.keys())
    while len(no_incoming) != 0:
        current_vertex = no_incoming.pop()
        result_list.append(current_vertex)
        outgoing_edges = []
        for to_vertex in graph.adjacency_list[current_vertex]:
            outgoing_edge = (current_vertex, to_vertex)
            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                no_incoming.append(to_vertex)
    return result_list

def all_pairs_shortest_path(graph):
    vertices = graph.get_vertex_list()
    num_vertices = len(vertices)
    dist_matrix = []
    for i in range(0, num_vertices):
        dist_matrix[i][i] = 0
    for edge in graph.edge_weights:
        dist_matrix[vertices.index(edge[0])][vertices.index(edge[1])] = graph.edge_weights[edge]
    for k in range(0, num_vertices):
        for toIndex in range(0, num_vertices):
            for fromIndex in range(0, num_vertices):
                currentLength = dist_matrix[fromIndex][toIndex]
                possibleLength = dist_matrix[fromIndex][k] + dist_matrix[k][toIndex]
                if possibleLength < currentLength:
                    dist_matrix[fromIndex][toIndex] = possibleLength
    return dist_matrix

def reconstruct_path(graph, start_vertex, end_vertex, dist_matrix):
    vertices = graph.get_vertex_list()
    start_index = vertices.index(start_vertex)
    path = []
    current_index = vertices.index(end_vertex)
    while current_index != start_index:
        incoming_edges = graph.get_incoming_edges(vertices[current_index])
        found_next = False
        for current_edge in incoming_edges:
            expected = dist_matrix[start_index][current_index] - graph.edge_weights[current_edge]
            actual = dist_matrix[start_index][vertices.index(current_edge[0])]
            if expected == actual:
                current_index = vertices.index(current_edge[0])
                path = [current_edge] + path
                found_next = True
                break
        if found_next == False:
            return None
    return path
