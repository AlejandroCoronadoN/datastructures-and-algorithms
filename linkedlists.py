
class Node:
  def __init__(self, data):
    self.data = data
    self.state = False
    self.next_node = None


class LinkedList:
  """This is an object that creates a Linked List and each component of the linked list is a Node.
  #* The advantages of a linked list is that we can insert items at the begining really fast and we 
  #* can use different types of data inseide the linked list.
  #* We don't need to resize the space of the linked list whenever we add more elements.
  #! Tha main disadvantage is that it doesn't have random access memory: i.e the items are not located next
  #! to each other in the memory.
  #! Also they require more memory in order to save the reference of each node that connects to the next node.
  #?
  #?
  
  """
  def __init__(self):
    self.head =  None
    self.nodeCount =0 
  
  def insert_start(self, data):
    self.nodeCount +=1 
    
    if not self.head:
      #Head is empty, we insert the first node
      self.head = Node(data)
    else:
      #Head is not empty
      newNode =  Node(data)
      newNode.next_node = self.head
      self.head = newNode
  def printNodes(self):
    next_node = self.head
    while next_node:
      print(next_node.data)
      next_node = next_node.next_node

  def insert_end(self, data):
    #We need to go all the way trough all the nodes untilm aswwe reach trhe last node that is marked 
    # by next_node == None
    actual_node = self.head 
    self.nodeCount +=1

    while actual_node.next_node:
      actual_node = actual_node.next_node
    
    actual_node.next_node = Node(data)
  
  #TODO : Create an algorith that finds the middle node without extra memory
  def find_middle_node(self):
    if self.head is not None:
      first_pointer = self.head
      second_pointer = self.head.next_node
      counter =0
      while second_pointer.next_node is not None:
        counter +=1
        if second_pointer.next_node.next_node is None:
          #We still return because we reach the end and we have a unpair array
          print(counter)
          return first_pointer.next_node
        else:
          #we move the pinters
          first_pointer = first_pointer.next_node
          second_pointer = second_pointer.next_node.next_node
        print(counter)
      return first_pointer
      
    else:
      return None

  def remove_node_all(self, data):
    """Iterates through the nodes until we find the Node with data== data and delete all the appearances

    Args:
        data ([type]): [description]
    """
    actual_node = self.head
    previous_node =None
    while actual_node:
      if actual_node.data ==  data:        
        self.nodeCount -=1
        if not previous_node:
          #head scenario
          self.head =  actual_node.next_node  
        else:
          previous_node.next_node =actual_node.next_node
      previous_node =  actual_node
      actual_node = actual_node.next_node

  def remove_node(self, data):
    """Iterates through the nodes until we find the Node with data== data and delete the first appearance

    Args:
        data ([type]): [description]
    """
    actual_node = self.head
    previous_node =None
    while actual_node:
      if actual_node.data ==  data:        
        self.nodeCount -=1
        if not previous_node:
          #head scenario
          self.head =  actual_node.next_node  
        else:
          previous_node.next_node =actual_node.next_node
        return
      previous_node =  actual_node
      actual_node = actual_node.next_node
      
linkedlist = LinkedList()
linkedlist.insert_start('a1')
linkedlist.insert_end('a2')
linkedlist.insert_end('m')
linkedlist.insert_end('e1')

linkedlist.printNodes()
middle_node = linkedlist.find_middle_node()
print(middle_node.data)


