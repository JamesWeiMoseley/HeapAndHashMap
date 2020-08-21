
class SLNode:
    def __init__(self, key: str, value: object) -> None:
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        # Return content of the node in human-readable form 
        return '(' + str(self.key) + ': ' + str(self.value) + ')'


class LinkedList:
    def __init__(self) -> None:
        # Init new SLL
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        # Return content of SLL in human-readable form
        content = ''
        if self.head is not None:
            content = str(self.head)
            cur = self.head.next
            while cur is not None:
                content += ' -> ' + str(cur)
                cur = cur.next
        return 'SLL [' + content + ']'

    def insert(self, key: str, value: object) -> None:
        # Insert new node at the beginning of the list
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key: str) -> bool:
        # Remove first node with matching key
        # Return True is some node was removed, False otherwise
        prev, cur = None, self.head
        while cur is not None:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def contains(self, key: str) -> SLNode:
        # If node with matching key in the list -> return pointer
        # to that node (SLNode), otherwise return None
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def length(self) -> int:
        return self.size

    def __iter__(self) -> SLNode:
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next


class DynamicArray:

    def __init__(self, arr=None):
        # Initialize new dynamic array
        self.data = arr.copy() if arr else []

    def __str__(self) -> str:
        return str(self.data)

    def append(self, value: object) -> None:
        self.data.append(value)

    def pop(self) -> object:
        return self.data.pop()

    def swap(self, i: int, j: int) -> None:
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def get_at_index(self, index: int) -> object:
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        self.data[index] = value

    def length(self) -> int:
        return len(self.data)
