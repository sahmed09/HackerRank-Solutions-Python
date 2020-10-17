class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)  # Create a new node, Put in the data, Set next as None

    # If the Linked List is empty, then make the new node as head
    if head is None:
        head = new_node
    else:
        # Else traverse till the last node
        last = head
        while last.next:
            last = last.next
        last.next = new_node  # Change the next of last node
    return head

# def insertNodeAtTail(head, data):
#     new_node = SinglyLinkedListNode(data)  # Create a new node, Put in the data, Set next as None
#
#     # If the Linked List is empty, then make the new node as head
#     if head is None:
#         head = new_node
#         return head
#
#     # Else traverse till the last node
#     last = head
#     while last.next:
#         last = last.next
#     last.next = new_node  # Change the next of last node
#     return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
