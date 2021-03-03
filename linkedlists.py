
class Node:
  def __init__(self, data):
    self.data = data
    self.state = False
    self.nextNode = None


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
      newNode.nextNode = self.head
      self.head = newNode
  def printNodes(self):
    nextNode = self.head
    while nextNode:
      print(nextNode.data)
      nextNode = nextNode.nextNode

  def insert_end(self, data):
    #We need to go all the way trough all the nodes untilm aswwe reach trhe last node that is marked 
    # by nextNode == None
    actual_node = self.head 
    self.nodeCount +=1

    while actual_node.nextNode:
      actual_node = actual_node.nextNode
    
    actual_node.nextNode = Node(data)
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
          self.head =  actual_node.nextNode  
        else:
          previous_node.nextNode =actual_node.nextNode
      previous_node =  actual_node
      actual_node = actual_node.nextNode

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
          self.head =  actual_node.nextNode  
        else:
          previous_node.nextNode =actual_node.nextNode
        return
      previous_node =  actual_node
      actual_node = actual_node.nextNode
      
linkedlist = LinkedList()
linkedlist.insert_start(6)
linkedlist.insert_start(7)
linkedlist.insert_start(8)
linkedlist.insert_start(10)
linkedlist.insert_end(7)
linkedlist.insert_end(8)
linkedlist.insert_end('end')

linkedlist.printNodes()
linkedlist.remove_node('end')
print('Delete some elements')
linkedlist.printNodes()

print('Delete some elements')
linkedlist.remove_node(7)
linkedlist.printNodes()

print('Delete some elements')
linkedlist.remove_node(10)
linkedlist.printNodes()

    