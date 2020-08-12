# Course: CS261 - Data Structures
# Assignment: 5
# Student: James Moseley
# Description: This is an implementation of a min heap using a dynamic array. 


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    #this function will add a new node onto a heap
    def add(self, node: object) -> None:
        self.heap.append(node)
        index = self.heap.length()-1
        parent = self.parent(index)
        if parent > -1:
            self.bubble_up(index, parent)

    #this bubble up will sort a heap every time a new node is added to the array by moving it up to the parents until
    # it has a parent that is smaller    
    def bubble_up(self, index, parent):
        while parent > -1:
            if self.heap.get_at_index(parent) > self.heap.get_at_index(index):
                self.heap.swap(parent, index)
            index = parent
            parent = self.parent(parent)
        
    #this will sort a an array to a min heap by iterating through all the numbers
    def sort(self):                         
        for i in range(self.heap.length()):
            index = i
            parent = self.parent(index)        
            if parent > -1:
                if self.heap.get_at_index(parent) > self.heap.get_at_index(index):
                    self.heap.swap(parent, index)
                    
    def parent(self, index):
        return (index-1)//2

    def left(self, index):
        return 2*index+1

    def right(self, index):
        return 2*index+2

    #in this function wil will simply sort the array, then return the first element
    def get_min(self) -> object:
        if self.heap.length() < 1:
            raise MinHeapException
        else:
            index = self.heap.length()-1
            parent = self.parent(index)
            self.bubble_up(index, parent)
            return self.heap.get_at_index(0)

    #in this function, we have to swap the first and the last element, this way we can pop it off the stack
    #after that we must resort the array before we can do it again
    def remove_min(self) -> object:
        if self.heap.length() < 1:
            raise MinHeapException
        else:
            min = self.heap.get_at_index(0)
            self.heap.swap(self.heap.length()-1, 0)
            self.heap.pop()
            self.sort()
            return min

    # this function takes an unsorted array, and builds a min heap that takes uses a bubble up time
    # It is different than the sort function that just gives us a simple min heap by switching parents and children
    def build_heap(self, da: DynamicArray) -> None:
        if self.heap.length()<= da.length():
            self.heap = DynamicArray()
            for i in range(da.length()):                    #will add the da onto the heap
                self.heap.append(da.get_at_index(i))
            index = self.heap.length()-1
            parent = self.parent(index)
            self.bubble_down(parent)
  
    #this function will percolate down by looking at parent nodes and moving them down if they are smaller than their children
    def bubble_down(self, parent):
        left = self.left(parent)
        right = self.right(parent)
        smallest = 0
        if self.heap.get_at_index(left) > self.heap.get_at_index(right):
            smallest = right
        else:
            smallest = left
        if parent >-1:          #it will keep running as long as the parent is 0 or more meaning it has reached the front of the array                                 
            while self.heap.get_at_index(parent) > self.heap.get_at_index(smallest):
                if self.heap.get_at_index(parent) > self.heap.get_at_index(smallest):
                    self.heap.swap(smallest, parent)
                    if self.left(smallest)< self.heap.length() or self.right(smallest)<self.heap.length():
                        temp = smallest
                        self.bubble_down(temp)                      #will call this if there are children underneath the node
            parent -=1
            self.bubble_down(parent)
            
            




       
       
        
        
      

