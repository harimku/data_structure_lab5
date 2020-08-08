from dynamic_array import DynamicArray

# node definition
class Node:
    def __init__(self, u=None, v=None, node=None):
        self.node = node
        self.prev = None
        self.next = None
        self.u = u
        self.v = v


# Implement Queue
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Queue Operations
    # inserts x at end of the queue
    def push(self, data):
        if self.tail is None:
            self.tail = data
            if self.head is None:
                self.head = data
            elif self.head is not None:
                self.head.next = self.tail
                self.tail.prev = self.head
        else:
            # tail exists
            if self.head is not None:
                self.tail.next = data
            data.prev = self.tail
            self.tail = data

        self.size += 1

        if self.size >= 2:
            vals = DynamicArray()
            runner = self.head
            while runner:
                vals.append((runner.u, runner.v, runner.node))
                runner = runner.next
            vals.sort(key=lambda item: item[2])
            runner = self.head
            i = 0
            while runner:
                runner.u = vals[i][0]
                runner.v = vals[i][1]
                runner.node = vals[i][2]
                runner = runner.next
                i += 1

    def pop(self):
        if self.head is None:
            print('There is no element to delete')
            return None
            # if head exists
        value = self.head.node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value
        self.head = self.head.next
        if self.head is None:
            return value
        self.head.prev = None
        return value

    # returns but does not remove item at the front of queue
    def peek(self):
        if self.head is None:
            print('There is no element in the queue')
            return None
        else:
            return self.head.node

    # returns true if queue has no items
    def isEmpty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    # returns the number of items in the queue
    def getLength(self):
        temp = self.tail
        count = 0
        while temp:
            count += 1
            temp = temp.prev
        return count

        # prints queue from tail(top) of queue

    def Output(self):
        rover = self.tail
        count = 0

        while (rover is not None):
            if rover.next is None:
                next_out = 'NULL'
            else:
                next_out = str(rover.next.node)
            if rover.prev is None:
                prev_out = 'NULL'
            else:
                prev_out = str(rover.prev.node)

            print('Node {} : data={}, prev={}, next={}'.format(str(count), str(rover.node), prev_out, next_out))
            count += 1
            rover = rover.prev
        if count == 0:
            print('<Empty Queue>')

    def __getitem__(self, key):
        if self.head is None:
            print('Head is None')
        else:
            runner = self.head
            for i in range(key):
                runner = runner.next
            return runner.u, runner.v, runner.node


def main():
    # Automated Test
    print('=============== Queue Implementation ===============')
    print('Operation: Creating Queue')
    que = PriorityQueue()
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: push({})'.format(str(0)))
    print('Operation: push({})'.format(str(1)))
    print('Operation: push({})'.format(str(2)))
    print('Operation: push({})'.format(str(3)))
    que.push(0)
    que.push(1)
    que.push(2)
    que.push(3)
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: getLength()')
    x = que.getLength()
    print('Length of current Queue: {}'.format(str(x)))
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: pop()')
    que.pop()
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: peek()')
    x = que.peek()
    print('Item at the front of Queue: {}'.format(str(x)))
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: isEmpty()')
    val = que.isEmpty()
    if val:
        print('Queue is empty')
    else:
        print('Queue is not empty')
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: pop()')
    que.pop()
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: pop()')
    que.pop()
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: pop()')
    que.pop()
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: isEmpty()')
    val = que.isEmpty()
    if val:
        print('Queue is empty')
    else:
        print('Queue is not empty')
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Operation: getLength()')
    x = que.getLength()
    print('Length of current Queue: {}'.format(str(x)))
    print('')
    print('Current Queue:')
    que.Output()
    print('=================================================================')
    print('Program Finished')


if __name__ == '__main__':
    main()
