class Node:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr = 0
        self.head = Node(-1,-1)
        self.tail = self.head
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            temp = self.dict[key]
            if temp is self.tail:
                return temp.val
            if temp.prev:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                temp.next = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            old_tail = self.tail
            self.tail.next = temp
            self.tail = self.tail.next
            temp.prev = old_tail
            if self.head is None:
                self.head = self.tail
            return self.tail.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            temp = self.dict[key]
            if temp is self.tail: 
                temp.val = value
                return
            temp.val = value
            if temp.prev:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                temp.next = None
            else:
                self.head = self.head.next
                self.head.prev = None
            old_tail = self.tail
            self.tail.next = temp
            self.tail = self.tail.next
            temp.prev = old_tail
        else:
            self.tail.next = Node(value, key, prev=self.tail)
            self.dict[key] = self.tail.next
            self.tail = self.tail.next
            self.curr += 1

        if self.curr >= self.capacity:
            if self.head.key in self.dict:
                del self.dict[self.head.key]
            self.head = self.head.next
            self.head.prev = None
            self.curr -= 1