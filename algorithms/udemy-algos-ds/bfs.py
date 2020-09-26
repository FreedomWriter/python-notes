class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class BreadthFirstSearch(object):
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.visited = True

        while queue:
            current_node = queue.pop(0)
            print(current_node.name)

            for neighbor in current_node.adjacencyList:
                if not neighbor.visited:
                    neighbor.visited = True
                    queue.append(neighbor)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2 )
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BreadthFirstSearch()
print(bfs.bfs(node1))