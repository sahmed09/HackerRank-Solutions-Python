import sys


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


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next


def mergeLists(head1, head2):
    mergedHead = SinglyLinkedListNode(1)  # dummy node so can be handled the same
    merged = mergedHead

    while head1 is not None or head2 is not None:
        if head1 is None:
            merged.next = head2
            break
        elif head2 is None:
            merged.next = head1
            break
        else:
            if head1.data < head2.data:
                merged.next = head1
                head1 = head1.next
            else:
                merged.next = head2
                head2 = head2.next
        merged = merged.next

    return mergedHead.next


# def mergeLists(head1, head2):
#     # get the correct first node and increment the pointer
#     if head1.data < head2.data:
#         head = head1
#         head1 = head1.next
#     else:
#         head = head2
#         head2 = head2.next
#     current = head
#
#     # while both of the lists have data
#     while head1 and head2:
#         # merge the lower value node
#         if head1.data < head2.data:
#             current.next = head1
#             head1 = head1.next
#         else:
#             current.next = head2
#             head2 = head2.next
#         # and update the pointer
#         current = current.next
#
#     # if there are nodes remaining in one of the lists, append it to the result
#     if head1:
#         current.next = head1
#     elif head2:
#         current.next = head2
#     return head


# Using Recursion: add this in __main__ while using recursion ""
# def mergeLists(head1, head2):
#     sys.setrecursionlimit(10000)
#     if head1 is None and head2 is None:
#         return None
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1
#     if head1.data < head2.data:
#         smallerNode = head1
#         smallerNode.next = mergeLists(head1.next, head2)
#     else:
#         smallerNode = head2
#         smallerNode.next = mergeLists(head1, head2.next)
#     return smallerNode


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
