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


def sortedInsert(head, data):
    if head:
        node = head
        new_node = DoublyLinkedListNode(data)

        while True:
            if node.data >= data:
                prev_node = node.prev

                if prev_node:
                    prev_node.next = new_node
                    new_node.prev = prev_node
                else:
                    node.prev = new_node
                    head = new_node

                new_node.next = node
                break

            if node.next is None:
                node.next = new_node
                new_node.prev = node
                break

            node = node.next
    return head


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ')
