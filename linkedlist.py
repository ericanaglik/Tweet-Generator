class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        #0(1) because it is returning its head as None and has only one action
        
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        #0(1) because it just adds one, once and has one action only.
        
        """Return the length of this linked list by traversing its nodes."""
        count = 0
        for item in self.items(): #0(n)
            count += 1 # 0(1) because it just adds one, once.
        return count # 0(1) returning count only once
            
    def append(self, item):
        #0(1) because no matter what happens, it does only one thing.
        
        """Insert the given item at the tail of this linked list."""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item) #0(1) because 
        if self.is_empty(): # the linkedlist is empty    It would also be 0(1) because if it is empty it will do one thing.
            self.head = new_node
            self.tail = new_node # Because linkedlist has 1 item it is also tail
        else: # If linkedlist is NOT empty  0(1) because it still only does one thing and does not loop.
            assert self.tail is not None
            self.tail.next = new_node #place previous tail's 'next' to new_node
            self.tail = new_node # Sets tail to new_node
        
    def prepend(self, item):
        
        # 0(1) because it only does something once, if it is None

        """Insert the given item at the head of this linked list."""
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None: #linkedlist was empty before Prepend
            self.tail = new_node # since linkedlist only has 1 item, it is the tail
        
    def find(self, quality):
        #Best Case: 0(1) Because if none is None, it returns none and does only one action
        #Worst Case: 0(n) Because if the node is not None then it goes to the next step and finds IF quality is True.
        
        """Return an item from this linked list satisfying the given quality."""

        node = self.head
        while node is not None:
            if quality(node.data) is True:
                return node.data
            else:
                node = node.next # reassigns the variable to iterate through the list
                return None #item satisfying quality was never found
        
    def delete(self, item):
        #Best Case: 0(1) Because if current_node is None is stops the while loop and has only one action.
        #Worst Case: 0(n) Because if each conditon is met then it goes through three times for current_node.c

        """Delete the given item from this linked list, or raise ValueError."""
        previous_node = None
        current_node = self.head
        
        while current_node.data is not None: # linked list isn't empty and current_node is not out of range
            if current_node.data == item: #current_node is the same as item
                if self.head == current_node:
                    self.head = current_node.next #reassign head
                else: #2nd node or later is a match
                prev_node = current_node # keep track of previous node before moving to the next
                current_node = current_node.next # iterate through the list
                
            raise ValueError('Item not found: {}'.format(item)) # did not find item
            
            

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
