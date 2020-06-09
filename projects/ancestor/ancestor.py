from util import Stack, Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
    #   s = [v,neightbor1, neightbor2]
        # LIFO
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for vertex in self.get_neighbors(v):
                    s.push(vertex)

    def dfs(self, starting_vertex, destination_vertex):
            """
            Return a list containing a path from
            starting_vertex to destination_vertex in
            depth-first order.
            """
            visited = set()
            path = [starting_vertex]
            if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
                return None
            if starting_vertex == destination_vertex:
                return path
            s = Stack()
            s.push(path)
            
            while s.size() > 0:
                path = s.pop()
                node = path[-1]
                if node not in visited:
                    visited.add(node)
                    for vertex in self.get_neighbors(node):
                        new_path = list(path)
                        new_path.append(vertex)
                        s.push(new_path)
                        if vertex == destination_vertex:
                            return new_path
        
    


    # '''
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # '''
    # ancesotrs [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push(starting_node)

    visited = set()
    parent = starting_node

    neighbor = get_neighbors1(starting_node, ancestors)
    if len(neighbor) < 1:
        return -1

    while s.size() > 0:
        popped = s.pop()
        parent = popped
        if popped not in visited:
            visited.add(popped)
            for popped in get_neighbors1(popped, ancestors):
                s.push(popped)
    
    return parent


def get_neighbors1(node, ancestors):
    neighbors = [ancestor[0] for ancestor in ancestors if ancestor[1] == node]
    return neighbors



    
print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9))