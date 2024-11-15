from LinkedList import Linkedlist
from Deque import Deque
from functions import reverse_file

def main():
    a = Linkedlist()
    a.insert(10, 0)
    print(a.find(10))
    a.insert(20,1)
    print(a)
    a.remove(20)
    print(a)
    b = Deque()
    b.appendleft(3)
    b.appendleft(4)
    b.appendleft(5)
    print(b)
    b.pop()
    print(b)
    b.pop()
    b.popleft()
    b.pop()
    reverse_file("output.txt", "input.txt")

if __name__ == '__main__':
    main()