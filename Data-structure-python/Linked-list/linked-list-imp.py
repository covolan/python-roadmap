'''
Listas linkadas possuem as seguintes vantagens:
    Array dinamico;
    Facilidade de inserção e remoção.

As desvantagens são:
    Acesso aleatorio não é permitido (busca binária não funciona);
    Possui espaço extra na memória para o apontador;
    Não é amigavel ao cache;
    Atravessar a lista ao contrário não é possivel;
    Acesso direto não é permitido;
    Procura de elemento é O(n);
    Organizar listas linkadas é custoso.

Operações basicas de listas linkadas:
    Remoção;
    Inserção;
    Busca;
    Display.
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next
        print(" ")
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_data, new_data):
        if self.head is None:
            return
        
        new_node = Node(new_data)
        if (prev_data == self.head.data):
            new_node.next = self.head.next
            self.head.next = new_node
            return
        
        head = self.head
        while(head.data != prev_data):
            head = head.next
            if head == None:
                return
        new_node.next = head.next
        head.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

if __name__ == '__main__':

    llist = LinkedList()

    for i in range(0, 5):
        llist.append(i)
    
    llist.push(-1)
    llist.insertAfter(2, 99)
    llist.printList()



