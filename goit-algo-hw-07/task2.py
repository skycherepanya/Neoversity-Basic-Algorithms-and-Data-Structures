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

def find_min_value(node):
    if node is None:
        return None

    current = node
    while current.left:
        current = current.left
        
    return current.value

if __name__ == "__main__":
    root = Node(42)
    keys = [18, 55, 9, 21, 60, 5, 2] 
    for key in keys:
        root = insert(root, key)

    print(f"Найменше значення в дереві: {find_min_value(root)}")