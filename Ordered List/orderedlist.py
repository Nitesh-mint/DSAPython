from Node import Node
"""
This models defines a Ordered Linked List that holds the collection of Nodes.
The List is in order fashion either Ascending or Descending.
"""
class OrderedList:
    """
    Represents a List which holds the collection of Nodes.
    """
    def __init__(self):
        """
        Initializes a list with no data setting the head of the list to None.
        """
        self.head = None
    def size(self):
        """
        Retrieves the size of the list.
        Returns: 
            The number of node with data.
        """
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count
    def is_empty(self):
        """
        Retrieves the condition of the emptyness of the list.
        Returns: 
            boolean if list is empty or not.
        """
        return self.head == None

    def peek(self):
        """
        Retrieves the item at the end of the list.
        """
        current = self.head

        if current == None:
            return None

        while current.get_next() is not None:
            current = current.get_next()
        return current.get_data()

    def search(self, item):
        """
        Retrieves the item if it is present in the list.
        Args:
            item: The data to be searched in the list. 
        Returns: 
            boolean if the item is present or not.
        """
        current = self.head
        found = False
        stop = False
        """
        Run the loop untill the current is None , found is fa
        se and stop is also false
        """
        while current != None and not found and not stop: 
            if current.get_data() == item:
                found = True
            else: 
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
            return found
    
    def add(self, item): 
        """
        Adds the new node to the list respecting the order.
        Args: 
            item: The new node to be added to the list. 
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item: 
                stop = True 
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else: 
            temp.set_next(current)
            previous.set_next(temp)

mylist = OrderedList()
mylist.add(5)
mylist.add(3)
mylist.add(12)
print(mylist.peek())
print(mylist.size())


