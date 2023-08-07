class Stack:
    def __init__(self):
        self.__stack = []
        
    def push(self, value):
        self.__stack.append(value)
    
    def pop(self):
        p = self.__stack[-1]
        del self.__stack[-1]
        return p
    
    def get_stack(self):
        for i in self.__stack:
            print(i)
            


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

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())