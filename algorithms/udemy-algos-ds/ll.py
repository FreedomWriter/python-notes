class LLNode():
    def __init__(self, value=None, next_node = None):
        self.value = value
        self.next_node = next_node

class LL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, value):
        new_node = LLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  
            old_head = self.head
            new_node.next_node = old_head
            self.head = new_node
        self.size += 1

    def insert_at_tail(self, value):
        new_node = LLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
        
            self.head = self.head.next_node
        self.size -= 1



    def print(self):

        if self.head is None and self.tail is None:
            print("list is empty!")

        else:
            cur_node = self.head

            while cur_node is not None:
                print(cur_node.value)
                cur_node = cur_node.next_node


ll = LL()

ll.insert_at_head("first inserted")
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
ll.insert_at_head("second inserted")
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
ll.insert_at_head("third inserted")
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
ll.insert_at_tail("added a tail!!")
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
print("removing head ....")
ll.remove_head()
ll.remove_head()
ll.remove_head()
ll.remove_head()
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
ll.print()
if ll.tail is not None:
    print("tail: ",ll.tail.value)
if ll.head is not None:
    print("head: ", ll.head.value)
