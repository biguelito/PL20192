class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class list:
    def __init__(self):
        self.first = None
        self.end = None

    def insert_first(self, data):
        node = Node(data)
        if self.first is None:
            self.end = self.first = node

        else:
            self.first.prev = node
            node.next = self.first
            self.first = node

    def insert_end(self, data):
        node = Node(data)
        if self.end is None:
            self.end = self.first = node

        else:
            self.end.next = node
            node.prev = self.end
            self.end = node

    def remove_first(self):
        if self.first != self.end:
            self.first.next.prev = None
            self.first = self.first.next

        elif self.first == self.end:
            self.first = self.first = None

        else:
            return print(None)

    def remove_end(self):
        if self.first != self.end:
            self.end.prev.next = None
            self.end = self.end.prev

        elif self.first == self.end:
            self.first = self.first = None

        else:
            return print(None)

    def print(self):
        if self.first is None:
            print(None)
        else:
            node = self.first
            while node is not None:
                print(node)
                node = node.next


lista = list()
op = 1
print("""opçao 1: inserir no começo/insert_first
opçao 2: inserir no fim/insert_end
opçao 3: remover do começo/remove_first
opçao 4: remover do fim/remove_end
opçao 5: printar a lista/print
opçao 0: sair/exit
""")
while op != 0:
    op = int(input('sua opçao: '))
    if op == 1:
        lista.insert_first(input())
    elif op == 2:
        lista.insert_end(input())
    elif op == 3:
        lista.remove_first()
    elif op == 4:
        lista.remove_end()
    elif op == 5:
        lista.print()
    elif op == 0:
        break
