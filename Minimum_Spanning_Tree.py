import Graph as g
import heapq


class EdgeWeight:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __le__(self, other):
        return self.weight <= other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __ne__(self, other):
        return self.weight != other.weight
    

class VertexSetCollection:
    def __init__(self, all_vertices):
        self.vertex_map = dict()
        for vertex in all_vertices:
            vertex_set = set()
            vertex_set.add(vertex)
            self.vertex_map[vertex] = vertex_set

    def __len__(self):
        return len(self.vertex_map)
    
    def get_set(self, vertex):
        return self.vertex_map[vertex]
    
    def merge(self, vertex_set1, vertex_set2):
        merged = vertex_set1.union(vertex_set2)
        for vertex in merged:
            self.vertex_map[vertex] = merged

def minimum_spanning_tree(graph):
    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)
    heapq.heapify(edge_list)
    vertex_sets = VertexSetCollection(graph.adjacency_list)
    result_list = []
    while len(vertex_sets) > 1 and len(edge_list) > 0:
        next_edge = heapq.heappop(edge_list)
        set1 = vertex_sets.get_set(next_edge.from_vertex)
        set2 = vertex_sets.get_set(next_edge.to_vertex)
        if set1 is not set2:
            result_list.append(next_edge)
            vertex_sets.merge(set1, set2)
    return result_list