class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next


# All we need to do is swap prev and next pointers for all nodes,
# change prev of the head (or start) and change the head pointer in the end.
# Time Complexity: O(N)
def reverse(head):
    while head.next:
        head.prev, head.next, head = head.next, head.prev, head.next
    head.next, head.prev = head.prev, None
    return head

# Using Recursion:
# def reverse(head):
#     if head is None:
#         return head
#     head.next, head.prev = head.prev, head.next
#
#     if head.prev is None:
#         return head
#     return reverse(head.prev)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ')
