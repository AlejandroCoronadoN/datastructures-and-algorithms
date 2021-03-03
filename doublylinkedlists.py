
class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None
    self.previousNode = None
  
  def isLast(self, node):
    return not node.nextNode
      
class DoublyLinkedLists:
  def __init__(self):
    self.head = None
    self.tail = None
    self.countNodes = 0
  
  def insert_start(self, data):
    self.countNodes +=1 
    newNode = Node(data)
    if self.head:
      self.head.previousNode = newNode
      newNode.nextNode =  self.head
      self.head = newNode
    else:
      self.head = newNode
      self.tail = self.head
      
  def insert_node_end(self, data):
    self.countNodes +=1 
    newNode = Node(data)
    
    if self.head:
      newNode.previousNode = self.tail
      self.tail.nextNode = newNode
      self.tail = newNode
      
    else:
      self.head = newNode
      self.tail = self.head
          
  def delete_node_begining(self):
    """Delete the first node at the head of the doubly linked list
    Modifies the previous elements
    Changes the head to the next in line
    """
    self.head = self.head.nextNode
    self.head.previousNode = None 
  
  def delete_node_end(self):
    """Delete the last node in the doubly linked list
    Changes the tail element to the previous of the current tail
    modifiest next node of the second to las item
  
    """
    actual_node = self.head
    seconLast = self.tail.previousNode
    seconLast.nextNode = None
    self.tail = seconLast 
    
    

  def traverse_forward(self):
    """It iterates trough all the nodes in the doubly linked list and print the data inside them
    it uses nextNode
    """
    actual_node = self.head
    nodelist =  []
    while actual_node is not None :
      print(actual_node.data)
      actual_node = actual_node.previousNode
      
  def traverse_backward(self):
    """It iterates trough all the nodes in the doubly linked list and print the data inside them
    it uses nextNode
    """
    actual_node = self.tail
    nodelist =  []
    while actual_node is not None :
      print(actual_node.data)
      actual_node = actual_node.previousNode

      
  def delete_selected_node(self, data):
    """Delete a particularnode based on the data stored in the node
    Special cases delete begining and end require to change the head and tail pointer
    """
    if self.head.data == data:
      this.delete_node_begining()
    else:
      actual_node = self.head.nextNode
      while actual_node:
        if actual_node.data == data:
          if not actual_node.nextNode:
            #actual_node is the last element
            self.tail = actual_node.previousNode
          else:
            actual_node.nextNode.previousNode =  actual_node.previousNode
          actual_node.previousNode = actual_node.nextNode
          return 
    
  

dll = DoublyLinkedLists()    
dll.insert_start('b1')
dll.insert_node_end('e1')
dll.insert_start('b2')
dll.insert_node_end('e2')
dll.insert_start('b3')
dll.insert_node_end('e3')

dll.delete_node_end()
dll.delete_node_begining()

dll.traverse_forward()
print('test3')     
dll.delete_selected_node('b1') 
dll.traverse_forward()
