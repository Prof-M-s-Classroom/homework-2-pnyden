import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next=None

    def __str__(self):
        return str(self.value)

class LinkedList:
   def __init__(self,value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1

   def __str__(self):
       return str(self.head)


   def append(self,value):
    new_node = Node(value)
    if(self.length == 0):
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
    return True

   def prepend(self,value):
    new_node = Node(value)
    if(self.length == 0):
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self.length += 1
    return True


   def delfirst(self):
       if self.length == 0:
           return None
       temp=self.head
       self.head=self.head.next
       temp.next=None
       self.length -= 1
       if self.length == 0:
           self.tail=None
       return temp

   def dellast(self):
    if self.length == 0:
        return None
    temp=self.head
    pre=self.head
    while temp.next:
        pre=temp
        temp=temp.next
    self.tail=pre
    self.tail.next=None
    self.length -= 1
    if self.length == 0:
        self.head=None
        self.tail=None
    return temp
    

   def print_list(self):
       temp=self.head
       while temp is not None:
           print(temp.value)
           temp=temp.next

   def insertatindex(self, index, value):
       if index < 0 or index > self.length:
           return False
       if index == 0:
           return self.prepend(value)
       if index == self.length:
           return self.append(value)
       new_node = Node(value)
       temp = self.head
       for i in range(index - 1):
           temp = temp.next
       # Insert the new node at the desired index
       new_node.next = temp.next
       temp.next = new_node

       # Increment the length of the linked list
       self.length += 1
       return True

   def deleteatindex(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.delfirst()
        if index == self.length - 1:
            return self.dellast()
        temp = self.head
        for i in range(index - 1):
            temp = temp.next

        # Delete the node at the specified index
        node_to_delete = temp.next  # The node to be deleted
        temp.next = temp.next.next  # Skip over the node to delete

        # Decrement the length of the linked list
        self.length -= 1
        return True



def test_linked_list_operations():
    # Initialize with a starting value of 10
    ll = LinkedList(10)  # Now the linked list will start with a single element: [10]

    # Test inserting at index 0 (prepend)
    ll.insertatindex(0, 5)
    print("After inserting 5 at index 0:", ll.print_list())  # Expected: [5, 10]

    # Test inserting at index 1
    ll.insertatindex(1, 15)
    print("After inserting 15 at index 1:", ll.print_list())  # Expected: [5, 15, 10]

    # Test inserting at index 1 again
    ll.insertatindex(1, 12)
    print("After inserting 12 at index 1:", ll.print_list())  # Expected: [5, 12, 15, 10]

    # Test inserting at index equal to length (append)
    ll.insertatindex(4, 20)
    print("After inserting 20 at index 4:", ll.print_list())  # Expected: [5, 12, 15, 10, 20]

    # Test deleting at index 1
    ll.deleteatindex(1)
    print("After deleting at index 1:", ll.print_list())  # Expected: [5, 15, 10, 20]

    # Test deleting at index 0 (first element)
    ll.deleteatindex(0)
    print("After deleting at index 0:", ll.print_list())  # Expected: [15, 10, 20]

    # Test deleting at the last index
    ll.deleteatindex(2)
    print("After deleting at the last index:", ll.print_list())  # Expected: [15, 10]

    # Test inserting at an invalid index (out of bounds)
    result = ll.insertatindex(5, 25)
    print("Inserting at invalid index 5:", result)  # Expected: False

    # Test deleting at an invalid index (out of bounds)
    result = ll.deleteatindex(10)
    print("Deleting at invalid index 10:", result)  # Expected: False


# Run the tests
test_linked_list_operations()

"""
s1 = Spaceship("Voyager",300)
s2 = Spaceship("Enterprise",300)
s3 = Spaceship("Atlantis",300)
s4 = Spaceship("Challenger",300)
s5 = Spaceship("Artemis",300)

mylinkedlist=LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
"""
