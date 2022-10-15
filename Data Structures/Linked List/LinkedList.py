class Node:

  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = self.head


  def Insert(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next

  def Delete(self, index):
    if index == 0:
      if self.tail == self.head:
        self.tail = self.head.next
      self.head = self.head.next
    else:
      currIndex = 0
      temp = self.head
      
      while (temp != None) and (currIndex != index - 1):
        temp = temp.next
        currIndex += 1
        

      if temp.next == self.tail:
        self.tail = temp
      temp.next = temp.next.next
    
  
  
  def PrintList(self):
    temp = self.head
    while temp != None:
      print(f"{temp.value} -->")
      temp = temp.next
    print("NULL")


  def Search(self, value):
    temp = self.head
    while temp != None:
      if temp.value == value:
        return True
      temp = temp.next
    return False



# Call methods
ll = LinkedList()
ll.Insert("A")
ll.Insert("B")
ll.Insert("C")
ll.Insert("D")
ll.Insert("E")
ll.Delete(1)
ll.Delete(2)
ll.PrintList()
print(ll.Search("L"))
print(ll.Search("C"))