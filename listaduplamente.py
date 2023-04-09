class Node:
    def __init__(self, data=None):
        self.data = data
        self.prox = None
        self.ant = None


class ListaDuplamente:

    def __init__(self, primeiroNode=None):
        self.primeiroNode = primeiroNode
        self.ultimoNode = primeiroNode
        self.iterator = primeiroNode
        self.size = 0 if primeiroNode is None else 1

    def addNode(self, data: any):

        novoNode = Node(data)
        if self.iterator is None:
            self.iterator = novoNode
        if self.primeiroNode is None:
            self.primeiroNode = novoNode
            self.ultimoNode = novoNode
        else:
            novoNode.ant = self.iterator
            novoNode.prox = self.iterator.prox
            if self.iterator.prox is not None:
                self.iterator.prox.ant = novoNode
            else:
                self.ultimoNode = novoNode
            self.iterator.prox = novoNode
        self.size += 1

    def insNode(self, data: any):

        novoNode = Node(data)
        if self.iterator is None:
            self.iterator = novoNode
        if self.primeiroNode is None:
            self.primeiroNode = novoNode
            self.ultimoNode = novoNode
        else:
            novoNode.ant = self.iterator.prev
            novoNode.prox = self.iterator
            if self.iterator.prev is not None:
                self.iterator.prev.prox = novoNode
            else:
                self.primeiroNode = novoNode
            self.iterator.prev = novoNode
        self.size += 1

    def elimNode(self):

        if self.iterator is not None:
            if self.iterator.prev is not None:
                self.iterator.prev.proximo = self.iterator.proximo
            else:
                self.firstNode = self.iterator.proximo
            if self.iterator.proximo is not None:
                self.iterator.proximo.prev = self.iterator.prev
            else:
                self.ultimoNode = self.iterator.prev
            self.iterator = self.iterator.proximo
            self.size -= 1

    def primeiro_Node(self):

        self.iterator = self.primeiroNode

    def ultimo_Node(self):

        self.iterator = self.ultimoNode

    def proxNode(self):

        if self.iterator is not None:
            self.iterator = self.iterator.proximo
            if self.iterator is None:
                return True
        return False

    def anttNode(self):
        if self.iterator is not None:
            self.iterator = self.iterator.prev
            if self.iterator is None:
                return True
        return False

    def posNode(self, position: int):

        if position <= 1:
            self.primeiro_Node()
        elif position >= self.size:
            self.ultimo_Node()
        else:
            currentPos = 1
            currentNode = self.primeiroNode
            while currentPos < position and currentNode is not None:
                currentNode = currentNode.prox
                currentPos += 1
            self.iterator = currentNode
        if self.iterator is None:
            return True
        return False

    def undefinedIterator(self):

        return self.iterator is None
