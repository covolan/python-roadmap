'''
Stacks possuem as seguintes vantagens:
    Facil de implementar(array);
    Memorias de pointers não necessárias(array).
    Dinâmico(llist)

Desvantagens:
    Não é dinâmico (array);
    Memoria necessaria para pointers(llist).

Aplicações:
    Todas aplicações que relembrem uma pilha ou fila.

'''

#imp array:
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)  
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def printStack(self):
        for i in self.stack:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    
    stack = Stack()
    for i in range(0, 5):
        stack.push(i)
    print("Print stack:")
    stack.printStack()
    print("peeking stack: \n", stack.peek())
    stack.pop()
    print("Print stack:")
    stack.printStack()
    print("is stack empty? -> ", end='')
    print(stack.isEmpty())
    print("Stack size: ", end='')
    print(stack.size())