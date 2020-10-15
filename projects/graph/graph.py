"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Vertices not found")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = []
        queue.append(starting_vertex)

        visited = set()
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        stack = []
        stack.append(starting_vertex)

        visited = set()
        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        # stack = []
        # stack.append(starting_vertex)

        # visited = set()
        pass

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            Current_Vertex = queue.dequeue()
            v = Current_Vertex[-1]
            if v not in visited:
                if v == destination_vertex:
                    return Current_Vertex
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    newPath = list(Current_Vertex)
                    newPath.append(neighbor)
                    queue.enqueue(newPath)

        # # Create an empty queue
        # qq = Queue()
        # # Create an empty set to store visited nodes
        # visited = set()
        # # Add A PATH TO the starting vertex_id to the queue
        # qq.enqueue([starting_vertex])
        # # While the queue is not empty...
        # while qq.size() > 0:
        #     # Dequeue, the first PATH
        #     path = qq.dequeue()
        #     # Grab the LAST VERTEX FROM THE PATH
        #     last_vertex = path[-1]
        #     # CHECK IF IT"S THE TARGET
        #     if last_vertex == destination_vertex:
        #         # IF SO, RETURN THE PATH
        #         return path
        #     # Check if it's been visited
        #     else:
        #         # If it has not been visited...
        #         if last_vertex not in visited:
        #             # Mark it as visited
        #             visited.add(last_vertex)
        #             neighbor = self.get_neighbors(last_vertex)
        #             # Then add A PATH TO all neighbors to the back of the queue
        #             for n in neighbor:
        #                 # Make a copy of the path before adding
        #                 copy_path = list(path)
        #                 # Add n to our copy
        #                 copy_path.append(n)
        #                 # Add new copy to our queue
        #                 qq.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
