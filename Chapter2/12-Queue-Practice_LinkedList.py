"""Make a Queue class using a linked list!
Make sure you pass the test cases too!"""


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        pass

    def insert_start(self, new_element):
        pass

    def insert_end(self, new_element):
        pass

    def delete_start(self):
        pass

    def delete_end(self):
        pass


class Queue:
    def __init__(self, head=None):
        self.storage = LinkedList(head)

    def enqueue(self, new_element):
        pass

    def peek(self):
        pass

    def dequeue(self):
        pass


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
