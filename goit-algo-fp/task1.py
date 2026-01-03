class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # 1. Реверсування
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Сортування злиттям (Merge Sort)
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_mid = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_mid)

        return self._merge(left, right)

    def _get_middle(self, head):
        if head is None: return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, a, b):
        if a is None: return b
        if b is None: return a

        if a.data <= b.data:
            result = a
            result.next = self._merge(a.next, b)
        else:
            result = b
            result.next = self._merge(a, b.next)
        return result

# 3. Об'єднання двох відсортованих списків
def merge_two_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    
    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1: tail.next = l1
    if l2: tail.next = l2
        
    res_list = LinkedList()
    res_list.head = dummy.next
    return res_list

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(20)
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    
    print("Звязний список:")
    ll.print_list()

    print("Реверс:")
    ll.reverse()
    ll.print_list()

    print("Відсортовано:")
    ll.sort()
    ll.print_list()
    
    ll2 = LinkedList()
    ll2.insert_at_end(2)
    ll2.insert_at_end(15)
    ll2.sort()

    print("Об'єднаний список:")
    merged = merge_two_lists(ll, ll2)
    merged.print_list()