# from chapter 6.6 Python: Graphs in the Zybooks for C950
class AdjacencyList(object):
    def __init__(self):
        self.adjacency_list = {}
        
    def add_vertex(self, new_vertex: str) -> None:
        self.adjacency_list[new_vertex] = []
        
    def add_directed_edge(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        edge = (to_vertex, weight)
        if edge not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(edge)
        
    def add_undirected_edge(self, vertex_a: str, vertex_b: str, weight: float) -> None:
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_distance(self, from_vertex: str, to_vertex: str) -> float:
        for edge in self.adjacency_list[from_vertex]:
            if edge[0] == to_vertex:
                return edge[1]
        return None

    def print_adjacency_list(self) -> None:
        for vertex in self.adjacency_list:
            print(f"Vertex {vertex}: ", end="\n")
            print(f"Length: {len(self.adjacency_list[vertex])}", end="\n")
            print(f"Neighbors: ", end="\n")
            for neighbor in self.adjacency_list[vertex]:
                print(f"{neighbor[0]}", end="\n")
            print()