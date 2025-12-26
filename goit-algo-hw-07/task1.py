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

def find_max_value(node):
    if node is None:
        return None

    current = node
    while current.right:
        current = current.right
        
    return current.value

if __name__ == "__main__":
    root = Node(15)
    keys = [10, 25, 6, 12, 20, 30, 4]
    for key in keys:
        root = insert(root, key)

    print(f"Найбільше значення в дереві: {find_max_value(root)}")