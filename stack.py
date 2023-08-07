class Stack:
    def __init__(self):
        self.__stack = []
        
    def push(self, value):
        self.__stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            p = self.__stack[-1]
            del self.__stack[-1]
            return p
        else:
            return None
    
    def get_stack(self):
        for i in self.__stack:
            return i
        
    def is_empty(self):
        return len(self.__stack) == 0
            


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
        
    def get_sum(self):
        return self.__sum
        
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
        
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        val = Stack.pop(self)
        if val is not None:
            self.__count += 1
        return val

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
stk.pop()
print(stk.get_counter())
# print(stk.get_stack())