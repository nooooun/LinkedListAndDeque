from LinkedList import Linkedlist

class Deque(Linkedlist):

    def remove(*args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal.")
    def insert(*args, **kwargs):
        raise NotImplementedError("Use appendleft() for adding.")

    def pop(self):
        try:
            if not self.tail:
                raise ValueError("Deque is empty.")
            value = self.tail.value
            if self.tail.prev:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = self.tail = None
            self.size -= 1
            return value
        except ValueError as e:
            print(f"Error:{e}")
            return None

    def popleft(self):
        try:
            if not self.head:
                raise ValueError("Deque is empty.")
            value = self.head.value
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = self.tail = None
            self.size -= 1
            return value
        except ValueError as e:
            print(e)
            return None

    def appendleft(self, value):
        self.push_forward(value)
