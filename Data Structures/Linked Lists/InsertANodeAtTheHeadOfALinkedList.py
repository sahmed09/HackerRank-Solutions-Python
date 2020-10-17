class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node):
    temp = node
    while temp:
        print(temp.data)
        temp = temp.next


def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)  # Allocate the Node & Put in the data
    new_node.next = head  # Make next of new Node as head
    head = new_node  # Move the head to point to new Node
    return head


# def insertNodeAtHead(head, data):
#     node = SinglyLinkedListNode(data)
#     if head:
#         node.next = head
#     return node


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
