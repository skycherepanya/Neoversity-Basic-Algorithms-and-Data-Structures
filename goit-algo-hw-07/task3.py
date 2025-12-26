class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def calculate_sum(node):
    if node is None:
        return 0
    
    return node.value + calculate_sum(node.left) + calculate_sum(node.right)

if __name__ == "__main__":
    root = Node(50)
    keys = [30, 20, 40, 70, 60, 80]
    for key in keys:
        root = insert(root, key)

    print(f"Загальна сума дерева: {calculate_sum(root)}")