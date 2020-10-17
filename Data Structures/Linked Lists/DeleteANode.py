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


def deleteNode(head, position):
    current = head
    # next will point to None if there is not another item in the list
    if position == 0:
        head = head.next
    else:
        # iterate to the right node
        for i in range(position-1):
            current = current.next
        # and alter the next pointer
        current.next = current.next.next
    return head


# Recursive way:
# def deleteNode(head, position):
#     if position == 0:
#         return head.next
#     head.next = deleteNode(head.next, position-1)
#     return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)
    print_singly_linked_list(llist1)

