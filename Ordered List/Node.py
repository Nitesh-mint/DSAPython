"""
This module defines a simple Node class to represent a node in a linked list.
Each node holds data and a reference to the next node in the list.
"""

class Node:
    """
    Represents a node in a linked list.

    Attributes:
        data: The data stored in the node. 
        next: A reference to the next node in the list(default is None).
    """
    def __init__(self, init_data, *args):
        """
        Initializes a new Node with the given data. 
        Args: 
            init_data: The data to store in the node.
        """
        self.data = init_data 
        self.next = None
    def get_data(self):
        """
        Retrieves the data stored in the Node. 
        Returns:
            The data stored in the node.
        """
        return self.data
    def get_next(self):
        """
        Retrieves the reference to the next node.
        Returns: 
            The next node in the list, or None if there is no next node. 
        """
        return self.next
    def set_data(self,new_data):
        """
        Updates the data in the node. 
        Args:
            new_data: The new data to store in the node.
        """
        self.data = new_data
    def set_next(self, new_next):
        """
        Updates the refernce to the next node. 
        Args:
            new_next: The new node to the reference as the next node.
        """
        self.next = new_next
