class Graph:

    class Node:
    
        def __init__(self, val):
            self.neighbors = []
            self.val = val

        def get_neighbors(self):
            return self.neighbors

    def __init__(self):
        self.nodes = dict()
        self.size = 0

    def add_node(self, val):
        node = self.Node(val)
        self.nodes[node.val] = node
        self.size += 1

    def add_edge(self, u, v):
        u.neighbors.append(node2)
        v.neighbors.append(node1)

    def get_node(self, val):
        return self.nodes.get(val, None)


    def depth_search(self, source, target):
        stack = []
        visited = dict()
        stack.append(source)

        while len(stack) > 0:
            current_node = stack.pop()
            neighbors = current_node.get_neighbors()
            visited[current_node] = True

            if current_node == target:
                return True

            for node in neighbors:
                if not node in visited:
                    stack.append(node)

        return False
    
    
class BST:
    class Node:

        def __init__(self, val):
            self.value = val
            self.left_child = None
            self.right_child = None
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = self.Node(val)
        else
            self.insert_util(val, self.root)

    def insert_util(self, val, current_node):
        if current_node is None:
            return self.Node(val)
        else:
            if current_node.value > val:
                current_node.right_child = self.insert_util(val, current_node.right_child)
            elif current_node.value <= val:
                current_node.left_child = self.insert_util(val, current_node.left_child)
        return self.root