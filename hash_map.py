
from a5_include import *


def hash_function_1(key: str) -> int:
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        for i in range(self.capacity-1):
            if self.buckets.get_at_index(i).head is not None:
                # print(self.buckets.get_at_index(i))
                temp = self.buckets.get_at_index(i).head
                self.buckets.get_at_index(i).remove(temp.key)
                self.size-=1
           
    #this function will return the value of the node that matches the key that is given
    def get(self, key: str) -> object:
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).head is not None:
                temp = self.buckets.get_at_index(i).head
                while temp is not None:
                    if temp.key == key:
                        return temp.value
                    else: 
                        temp = temp.next        #this if chcking the linked list that was from a collision
        return None
    
    def dynamicList(self):
        return self.buckets.get_at_index(index).head

    def index(self, key):
        return self.hash_function(key) % self.capacity

    def put(self, key: str, value: object) -> None:
        index = self.index(key)                                         #this will insert into a empty list
        if self.buckets.get_at_index(index).head is None:
            self.buckets.get_at_index(index).insert(key, value)
            self.size +=1
        elif self.buckets.get_at_index(index).contains(key):          #this will replace the node
            self.buckets.get_at_index(index).insert(key, value)
        else:                                                   #this will insert a new node into a non empty list
            self.buckets.get_at_index(index).insert(key, value)
            self.size +=1
    
    #this function will remove a node if the ket matches
    def remove(self, key: str) -> None:
        if self.contains_key(key) is True:
            for i in range(self.capacity):
                temp = self.buckets.get_at_index(i)
                if temp.head is not None:
                    temp.remove(key)
            self.size -=1           #will decrease size if something is removed
                
                    
    #return true or false if a matching key if found
    def contains_key(self, key: str) -> bool:
        if self.buckets.length() == 0:
            return False
        else:
            index = self.index(key)
            for i in range(self.capacity):
                temp = self.buckets.get_at_index(i).head
                if temp is not None:
                    while temp is not None:
                        if temp.key == key:
                            return True
                        else:
                            temp = temp.next  
            return False

    #empty buckets is how many empty slots are in the dynamic array
    #it is different than size because it does not count for collision cases
    def empty_buckets(self) -> int:
        count = 0
        for i in range(self.capacity):
            if self.buckets.get_at_index(i).head is None:
                count +=1
        return count

    #table load is a formla of size/capacity
    def table_load(self) -> float:
        return self.size/self.capacity

    #resize table will increase the capacity of the dynamic array
    def resize_table(self, new_capacity: int) -> None:
        dif = new_capacity-self.capacity
        if dif > 0:
            self.capacity += dif
            for i in range(dif):
                self.buckets.append(LinkedList())
       
        
    #get keys will return a dynamic array of all the keys
    def get_keys(self) -> DynamicArray:
        d = DynamicArray()
        for i in range(self.capacity):
            temp = self.buckets.get_at_index(i).head
            if temp is not None:
                d.append(temp.key)
                while temp.next is not None:    #here we check for longer linked lists
                    temp = temp.next
                    d.append(temp.key)
        return d


