class AdjacencyList(object):
    '''
    Adjacency List implemented from:
    # Source: chapter 6.6 Python: Graphs in the Zybooks for C950.
    Changed it so the edge weights are added directly to each of the edges.

    '''
    def __init__(self):
        self.adjacency_list = {}
        
    def add_vertex(self, new_vertex: str) -> None:
        '''
        Adds a new vertex to the adjacency list.

        Parameters:
        new_vertex (str): The vertex to be added (an address in the context of this program)
        
        '''
        self.adjacency_list[new_vertex] = []
        
    def add_directed_edge(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        '''
        Adds a directed edge to the adjacency list.

        Parameters:
        from_vertex (str): The 'from' address.
        to_vertex (str): The 'to' address.
        weight (float): The distance (weight) from the 'from' address to the 'to' address.

        '''
        edge = (to_vertex, weight)
        if edge not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(edge)
        
    def add_undirected_edge(self, vertex_a: str, vertex_b: str, weight: float) -> None:
        '''
        Adds an undirected edge to the adjacency list. It does this by calling self.add_directed_edge
        on the vertexes going from point a to b, as well as from point b to a.

        Parameters:
        from_vertex (str): The 'from' address.
        to_vertex (str): The 'to' address.
        weight (float): The distance (weight) from the 'from' address to the 'to' address.
         
        '''
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_distance(self, from_vertex: str, to_vertex: str) -> float:
        '''
        Returns the distance (weight) from the 'from' address to the 'to' address.

        Parameters:
        from_vertex (str): The 'from' address.
        to_vertex (str): The 'to' address.

        Returns:
        float: Returns the distance (weight) from the 'from' address to the 'to' address.
        '''
        for edge in self.adjacency_list[from_vertex]:
            if edge[0] == to_vertex:
                return edge[1]
        return None