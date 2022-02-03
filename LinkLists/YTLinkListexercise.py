# from https://youtu.be/FSsriWQ0qYE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # initial value points to None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:      # while the cur_node is not 'Null' - continue loop
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:   # head pointer doesnt point to anything, so there is no node
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:   # while the next node is not 'Null' - continue loop
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        # point new node to old head of list
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        # verify that prev_node is there
        if not prev_node:
            print("Previous nod is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
#####################################################

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.insert_after_node(llist.head.next, "E")
llist.print_list()