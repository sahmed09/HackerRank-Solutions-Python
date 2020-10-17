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


"""To solve this problem, we must traverse the list using two pointers that we'll refer to as slow and fast. Our slow
pointer moves forward 1 node at a time, and our fast pointer moves forward 2 nodes at a time. If at any point
in time these pointers refer to the same object, then there is a loop; otherwise, the list does not contain a loop.
here we didn't use slow.. instead use head directly as second pointer."""


def has_cycle(head):
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        head = head.next

        if head == fast:
            return True
    return False
# Time Complexity: O(N)

# def has_cycle(head):
#     nodes = set()
#     while head is not None:
#         if head in nodes:
#             return 1
#         nodes.add(head)
#         head = head.next
#     return 0


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)
        print(result)

"""
Input:
1
1
3
1
2
3
Output: 1

Input:
1
-1
1
1
Output: 0"""
