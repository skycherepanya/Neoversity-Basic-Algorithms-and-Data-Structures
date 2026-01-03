import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція додавання ребер для малювання
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Відтінки
hex_colors = ['#111111', '#333333', '#555555', '#777777', '#999999', '#BBBBBB', '#DDDDDD']

def dfs_visualize(root):
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node:
            node.color = hex_colors[count] if count < len(hex_colors) else "#EEEEEE"
            count += 1
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
    draw_tree(root, "DFS (пошук в глибину)")

def bfs_visualize(root):
    queue = deque([root])
    count = 0
    while queue:
        node = queue.popleft()
        if node:
            node.color = hex_colors[count] if count < len(hex_colors) else "#EEEEEE"
            count += 1
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    draw_tree(root, "BFS (пошук в ширину")

# Створюємо дерево вручну
root = Node(0)
root.left = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)
root.right = Node(4)
root.right.left = Node(5)

# Спочатку малюємо BFS
print("Малюємо BFS...")
bfs_visualize(root)

# Скидаємо кольори для DFS
root = Node(0)
root.left = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)
root.right = Node(4)
root.right.left = Node(5)

print("Малюємо DFS...")
dfs_visualize(root)