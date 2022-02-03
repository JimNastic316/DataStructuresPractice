class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

#This insert function cuts off the list and needs to be fixed
#This insert function cuts off the list and needs to be fixed
def insert(value, head, index):
    cur = head
    print("value = {}, head = {}, index = {}".format(value, head, index))
    for i in range(index):
        cur = cur.next
        print('cur.next = {}'.format(cur.next))
    cur.next = Node(value)


# def insert(value, head, index):
#     cur = head
#     print('cur = head = {}'.format(head))
#     for i in range(index):
#         new_node = Node(head)
#         new_node.next = cur.next
        # new_node.val = value
        # cur.next = new_node
        # print('i = {} cur = {} cur.next = {}'.format(i, cur, cur.next))
        # cur = cur.next
        # print('cur = cur.next = {}'.format(cur))
    # cur.next = Node(value)

def print_list(head):
    cur = head
    while cur != None:
        cur = cur.next
        if cur != None:
            print(cur.val)
    print("End of list.\n")


#Build a simple list
head = Node()
cur = head

for i in range(5):
    cur.next = Node()
    cur = cur.next
    cur.val = i

print_list(head)
insert("Hi!", head, 3)

#This should print 0, 1, 2, Hi!, 3, 4, End of list. but our insert
#cuts off the tail of the list
print_list(head)
