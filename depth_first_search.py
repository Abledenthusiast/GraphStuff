
class Node:
    
    def __init__(self, val):
        self.neighbors = []
        self.val = val


class Graph:


    def __init__(self, nodes):
        self.nodes = dict(nodes)

    def add_node(self, node):
        self.nodes[val] = node

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

            if source == target:
                return True

            for node in neighbors:
                if not node in visited:
                    stack.append(node)

        return False




class Node:

    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None
    
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else
            self.insert_util(val, self.root)

    def insert_util(self, val, current_node):
        if current_node is None:
            return Node(val)
        else:
            if current_node.value > val:
                current_node.right_child = self.insert_util(val, current_node.right_child)
            elif current_node.value <= val:
                current_node.left_child = self.insert_util(val, current_node.left_child)
        return self.root