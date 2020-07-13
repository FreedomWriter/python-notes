# linked list implementation - THIS IS NOT FULLY FLESHED OUT

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None # Stores a node, that corresponds to our first node in the list
    self.tail= None # stores a node tht is the end of the list

  def add_to_head(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # new_node should point to current head
      new_node.next_node = self.head
      # move head to new_node
      self.head = new_node

  def add_to_tail(self, value):
    # create a node to add
    new_node = Node(value)
    # check if list is empty
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # point thendoe at the current tail, to the new node
      self.tail.next_node = new_node
      self.tail = new_node

# remove head and return it's value
  def remove_head(self, value):
    # if list is empty do nothing
    if not self.head:
      return None
    # if list only has one element set head and tail to None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
     # otherwise we have more elements in the list 
    else: 
      head_value = self.head.value
      self.head= self.head.next_node
      return head_value

  def contains(self, value):
    if self.head is None:
      return False

    # Loop through each node, until we see the value, or we cannot go further
    current_node = self.head
    while current_node is not None:
      # check if ths is the node we are looking format
      if current_node.value == value:
        return True

      #otherwise go to the next Node
      current_node = current_node.next_node
    #if we exit the loop without finding a value 
    return False


linked_list = LinkedList()
linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(linked_list.head.value)
print(linked_list.tail.value)
print(f'does our LLcontain 0? {linked_list.contains(0)}')
print(f'does our LLcontain 1? {linked_list.contains(1)}')
print(f'does our LLcontain 3? {linked_list.contains(3)}')
linked_list.add_to_head(2)
print(f'does our LLcontain 2 after adding it to the head? {linked_list.contains(2)}')
linked_list.remove_head(2)
print(f'does our LLcontain 2 after removing the head? {linked_list.contains(2)}')