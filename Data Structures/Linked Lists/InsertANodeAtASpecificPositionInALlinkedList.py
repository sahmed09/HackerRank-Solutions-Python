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


def insertNodeAtPosition(head, data, position):
    node = head
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        return new_node
    count = 1
    while count < position and node:
        count += 1
        node = node.next
    new_node = SinglyLinkedListNode(data)
    new_node.next = node.next
    node.next = new_node
    return head


# def insertNodeAtPosition(head, data, position):
#     new_node = SinglyLinkedListNode(data)
#     temp = head
#     if position == 0:
#         temp = new_node
#         return temp
#     else:
#         position = position - 1
#         while position > 0:
#             temp = temp.next
#             position -= 1
#         new_node.next = temp.next
#         temp.next = new_node
#         return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist_head)
