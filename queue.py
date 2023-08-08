class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.is_empty():
            val = self.__queue[-1]
            del self.__queue[-1]
            return val
        else:
            raise QueueError
    
    def is_empty(self):
        return len(self.__queue) == 0
    


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
