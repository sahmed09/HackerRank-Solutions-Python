class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next


def removeDuplicates(head):
    if head:
        root = head
        while root.next:
            if root.data == root.next.data:
                root.next = root.next.next
            else:
                root = root.next
    return head


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1)

        # Time Complexity: O(N)
