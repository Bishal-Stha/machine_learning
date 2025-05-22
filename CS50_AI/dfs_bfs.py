class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()
        stack = Stack()
        stack.push(start_node)

        while not stack.is_empty():
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                if node in self.graph:  # Check if node exists in graph
                    for neighbor in reversed(self.graph[node]):
                        if neighbor not in visited:
                            stack.push(neighbor)
        print()

    def bfs(self, start_node):
        visited = set()
        queue = Queue()
        queue.enqueue(start_node)
        visited.add(start_node)

        while not queue.is_empty():
            node = queue.dequeue()
            print(node, end=" ")

            if node in self.graph:  # Check if node exists in graph
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.enqueue(neighbor)
        print()


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Print graph visualization
    print("\nGraph visualization:")
    print("    1")
    print("   /   \\")
    print("  0 --- 2 --- 3")
    print("        |     |") 
    print("        \\_____/")

    print("\nDepth-First Search (DFS):")
    g.dfs(2)

    print("\nBreadth-First Search (BFS):")
    g.bfs(2)
