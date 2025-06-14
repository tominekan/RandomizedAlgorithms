"""
Linked List
---

This is an implementation of a doubly linked list
"""
from typing import Optional

class ListNode:
    def __init__(self, value, next: Optional["ListNode"], prev: Optional["ListNode"]):
        """
        Single node in the linked list

        ---
        O(1)
        """
        self.value = value
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f"Node with value: {self.value}"


class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list

        ---
        O(1)
        """

        self.head = None
        self.tail = None
        self.length = 0
    
    def add_head(self, value):
        """
        Adds an item to the head of the Linked List

        ---
        O(1) time
        """

        new_head = ListNode(value, self.head, None)

        if (self.head != None):
            self.head.prev = new_head

        self.head = new_head
        self.length += 1

        if (self.length == 1):
            self.tail = self.head
    
    def remove_head(self):
        """
        Removes the head of the Linked List. Returns the removed head

        ---
        O(1) time
        """

        if self.length < 1:
            raise Exception("Cannot call remove_head on empty LinkedList")
        
        old_head = self.head
        new_head = self.head.next
        self.head = new_head
        self.head.prev = None

        self.length -= 1
        return old_head
    
    def add_tail(self, value):
        """
        Adds an item to the tail of the Linked List

        ---
        O(1) time
        """

        new_tail = ListNode(value, next=None, prev=self.tail)

        if (self.tail != None):
            self.tail.next = new_tail

        self.length += 1

        if (self.length == 1):
            self.tail = self.head

        self.tail = new_tail
    
    def remove_tail(self):
        """
        Removes the tail of the Linked List

        ---
        O(1) time
        """

        if self.length < 1:
            raise Exception("Cannot call remove_tail on empty LinkedList")

        old_tail = self.tail
        new_tail = self.tail.prev
        self.tail = new_tail
        self.tail.next = None

        self.length -= 1
        return old_tail
    
    def in_linked_list(self, value):
        """
        Checks if `value` is in the linked list

        ---
        O(n) time
        """

        curr = self.head

        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next

        return False
    
    def search(self, value):
        """
        Searches Linked List `value` for value. Returns the node corresponding to it. 
        If `value` is not in Linked List, it returns None.

        ---
        O(n)
        """

        curr = self.head

        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        
        return None
    
    def remove(self, value):
        """
        Removes and returns the first instance of `value` in the Linked List. 
        If the value doesn't exist, do nothing lol.

        ---
        O(n)
        """

        if (self.length < 1):
            raise Exception("Cannot call remove on empty list")
        
        node_to_remove = self.search(value)
        if node_to_remove is not None:

            node_before = node_to_remove.prev
            node_after = node_to_remove.next

            if node_before is not None:
                node_before.next = node_after
            
            if node_after is not None:
                node_after.prev = node_before
            
            # We're removing the first element
            if (self.head == node_to_remove):
                self.head = node_after

            # We're removing the last eleemnt
            if (self.tail == node_to_remove):
                self.tail = node_before
            
            self.length -= 1
            return node_to_remove
        
        return None
    
    def remove_all(self, value):
        """
        Removes all instances of `value` in the Linked List. 
        Returns the number of instances of `value`
        If the value doesn't exist, do nothing.

        ---
        O(n)
        """

        if (self.length < 1):
            raise Exception("Cannot call remove on empty list")
        
        # Keep removing these values until there's nothing left
        curr = self.head
        num_instances = 0
        while curr is not None:
            if curr.value == value:
                num_instances += 1
                node_before = curr.prev
                node_after = curr.next

                # Can't access null elements
                if node_before is not None:
                    node_before.next = node_after

                # We need to remove the first element
                if self.head == curr:
                    self.head = node_after
            

                # Can't access null elements
                if node_after is not None:
                    node_after.prev = node_before

                # We need to remove the last element
                if self.tail == curr:
                    self.tail = node_before

                self.length -= 1

                curr = node_after
            else:
                curr = curr.next
        
        return num_instances
        
    def __len__(self):
        """
        Returns the number of items in the linked list

        ---
        O(1) time
        """

        return self.length
    
    def __str__(self):
        """
        Returns the string representation of the LinkedList.
        It makes the assumption that the values inside can be converted to string

        ---
        O(n) time
        """

        curr = self.head
        output = ""

        # Go until the second to last element
        if curr is not None:
            while curr.next is not None:
                output += str(curr.value) + " <-> "
                curr = curr.next

            output += str(curr.value)
        
        return output
    
    def __contains__(self, value):
        """
        Same as in_linked_list.

        ---
        O(n)
        """

        return self.in_linked_list(value)
    


def sample_cases():
    """
    Supa weak testing lol
    """

    print("Adding 5 items to linked list ... ")
    l = LinkedList()
    l.add_head("lebron")
    print(l)
    l.add_tail("james")
    print(l)
    l.add_tail("is")
    print(l)
    l.add_tail("da")
    print(l)
    l.add_tail("goat")
    print(l)
    print(f"New Length: {len(l)}\n")


    print("Removing 4 items from linked list ...")
    old_head = l.remove_head()
    print(l)
    print(f"Removed Item: {old_head}")

    old_tail = l.remove_tail()
    print(l)
    print(f"Removed Item: {old_tail}")
    print(f"New Length: {len(l)}\n")

    old_head = l.remove_head()
    print(l)
    print(f"Removed Item: {old_head}")

    old_head = l.remove_head()
    print(l)
    print(f"Removed Item: {old_head}")

    print("Peeking Linked List")
    print(f"Head: {l.head}")
    print(f"Tail: {l.tail}\n")

    print("Checking in_linked_list ...")
    print(f"lebron in Linked List: {l.in_linked_list('lebron')}")
    print(f"da in Linked List: {l.in_linked_list('da')}")
    print(f"1 in Linked List: {l.in_linked_list(1)}\n")

    print("Adding some more BS ... ")
    l.add_head("meet")
    l.add_tail("fookin")
    l.add_tail("crew")
    print(f"({len(l)} items): {l}")

    print(f"Removing 'fookin' ...")
    l.remove('fookin')
    print(f"({len(l)} items): {l}")

    print(f"Removing 'leanon' ...")
    l.remove('leanon')
    print(f"({len(l)} items): {l}\n")

    print("About to test remove_all: ")
    l.add_head("dabo")
    l.add_tail("dabo")
    l.add_head("1")
    l.add_tail("2")
    l.add_head("dabo")
    l.add_head("dabo")
    l.add_tail("3")
    l.add_tail("dabo")
    print(f"({len(l)} items): {l}")
    print("Removing all 'dabo'")
    l.remove_all("dabo")
    print(f"({len(l)} items): {l}\n")

