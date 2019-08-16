class Queue:
    ''' Implementation of a queue based on a python list class
where start of the list is to front/bottom end of the queue and
the end of the list is the rear/top end of the queue'''
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        # this will raise an indexerror exception when the queue is empty
        return self.__queue.pop(0)
    def size(self):
        return len(self.__queue)
    def peek(self):
        # this will raise an indexerror exception when the queue is empty
        return self.__queue[0]
    def isEmpty(self):
        return len(self.__queue) == 0
    def __str__(self):
        retValue = "[ "
        for k in range(len(self.__queue)-1):
            retValue += str(self.__queue[k]) + ","
        retValue += str(self.__queue[k+1]) + ' ]'
        return retValue


def main():
    ''' Test code to test the Queue class'''
    q = Queue()
    assert(q.isEmpty())
    assert(q.size() == 0)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert(q.size() == 3)
    assert( not q.isEmpty())
    assert(q.peek() == 10)
    assert(q.dequeue() == 10)
    assert(q.size() == 2)
    assert(q.peek() == 20)
    assert(q.dequeue() == 20)
    assert(q.dequeue() == 30)
    try:
        q.dequeue()
    except Exception as e:
        print("q.dequeue caused exception:",e)
    print("All tests pass")

if (__name__ == "__main__"):
    main()

