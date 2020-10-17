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
        print(node.data)
        node = node.next


# def getNode(head, positionFromTail):
#     index = 0
#     result = head
#     while head.next:
#         head = head.next
#         if index >= positionFromTail:
#             result = result.next
#         index += 1
#     return result.data
# Time Complexity: O(N)


# def getNode(head, positionFromTail):
#     count = 0
#     temp = head
#     while head.next:
#         head = head.next
#         count += 1
#     for i in range(count-positionFromTail):
#         temp = temp.next
#     return temp.data


def getNode(head, positionFromTail):
    # traverse the list and create an array. This process needs a lot of memory.
    ans = []
    while head:
        ans.append(head.data)
        head = head.next
    return ans[-positionFromTail-1]


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)
        print(result)
