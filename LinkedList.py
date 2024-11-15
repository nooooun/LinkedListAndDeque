class Node:
    def __init__(self, value):
        if not isinstance(value, (int, float, str)):
            raise TypeError(f"Value: {value} is not int, float or str type.")
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return repr(self.value)

class Linkedlist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        tempList = []
        while temp is not None:
            tempList.append(temp.value)
            temp = temp.next
        return str(tempList)

    def __len__(self):
        return self.size

    def push_back(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def push_forward(self, value):
        newNode = Node(value)
        if self.tail is None:
            self.tail = newNode
            self.head = self.tail
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def insert(self, value, index):
        try:
            if index < 0 or index > self.size:
                raise IndexError("Wrong index")
            newNode = Node(value)
            if index == 1:
                self.push_forward(value)
            elif index == self.size:
                self.push_back(value)
            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                newNode.prev = temp.prev
                newNode.next = temp
                if temp.prev is not None:
                    temp.prev.next = newNode
                temp.prev = newNode
            self.size += 1
        except IndexError as e:
            print('Error: ', e)
            return

    def pop_back(self):
        if self.tail is None:
            return
        else:
            self.tail.prev.next = None
            self.tail.prev = None
            self.size -= 1

    def pop_forward(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            self.size -= 1


    def find(self, value) -> Node:
        current = self.head
        try:
            while current:
                if current.value == value:
                    return current
                current = current.next
        except ValueError as e:
            print(f"Error: {e}")

    def get(self, index) -> Node:
        current = self.head
        try:
            for i in range(index):
                current = current.next
            return current
        except IndexError as e:
            print(f"Error: {e}")

    def remove(self, value):
        try:
            current = self.find(value)
            if not current:
                raise ValueError(f"List does not contain {value}")
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
            self.size -= 1
        except ValueError as e:
            print('Error: ', e)
            return


    def clear(self):
        self.size = 0
        self.head = None
        self.tail = None