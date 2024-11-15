from Deque import Deque

def reverse_file(out_file, in_file):
    stack = Deque()
    with open(in_file) as input_file:
        text = input_file.readlines()
    for i in text:
        stack.appendleft(i)
    with open(out_file, 'w') as output_file:
        while stack:
            output_file.write(stack.pop())