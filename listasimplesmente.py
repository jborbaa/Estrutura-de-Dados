from listaduplamente import ListaDuplamente


class ListaNode:

    def __init__(self, data, listaDE: ListaDuplamente, proxNode=None):
        self.data = data
        self.listaDE = listaDE
        self.proxNode = proxNode


class ListaSimplesmente:

    def __init__(self, primeiroNode=None):
        self.primeiroNode = primeiroNode
        self.ultimoNode = primeiroNode
        self.iterator = primeiroNode
        if primeiroNode:
            self.size = 1
        else:
            self.size = 0

    def addNode(self, data: any, listaDE: ListaDuplamente):

        novoNode = ListNode(data, listaDE)
        novoNode.proxNode = None
        if self.size == 0:
            self.iterator = novoNode
            self.primeiroNode = novoNode
            self.ultimoNode = novoNode
        elif self.iterator == self.ultimoNode:
            self.ultimoNode.proxNode = novoNode
            self.iterator = novoNode
            self.ultimoNode = novoNode
        else:
            novoNode.proxNode = self.iterator.proxNode
            self.iterator.proxNode = novoNode
            self.iterator = novoNode

        if listaDE != None:
            novoNode.listaDE = listaDE
        self.size += 1
        return True

    def insNode(self, data, ListaDE: ListaDuplamente):

        novoNode = ListNode(data, ListaDE)
        novoNode.proxNode = None
        if self.size == 0:
            self.iterator = novoNode
            self.primeiroNode = novoNode
            self.ultimoNode = novoNode
        elif self.iterator == self.primeiroNode:
            novoNode.proxNode = self.primeiroNode
            self.proxNode = novoNode
            self.iterator = novoNode
        else:
            currentNode = self.primeiroNode
            while currentNode.proxNode != self.iterator:
                currentNode = currentNode.proxNode
            novoNode.proxNode = self.iterator
            currentNode.proxNode = novoNode
            self.iterator = novoNode
        self.size += 1
        return True

    def elimNode(self):

        if self.iterator == self.proximoNode:
            if self.ultimoNode == self.proximoNode:
                self.ultimoNode = None
                self.proxNode = None
                self.iterator = None
            else:
                self.primeiroNode = self.primeiroNode.proxNode
                self.iterator.proxNode = None
                self.iterator = self.primeiroNode
        else:
            currentNode = self.primeiroNode
            while currentNode.proxNode != self.iterator:
                currentNode = currentNode.proxNode
            if self.iterator == self.ultimoNode:
                self.ultimoNode = currentNode
                self.iterator.proxNode = None
                self.iterator = None
                currentNode.proxNode = None
            else:
                currentNode.proxNode = self.iterator.proxNode
                currentNode = self.iterator
                self.iterator = self.iterator.proxNode
                currentNode.proxNode = None
        self.size = self.size - 1
        return True

    def primeiro_Node(self):

        self.iterator = self.primeiroNode
        return True

    def ultimo_Node(self):
        self.iterator = self.ultimoNode
        return True

    def proxNode(self):

        if self.iterator:
            self.iterator = self.iterator.proxNode
        return True

    def posNode(self, position: int):

        if position > 0 and position <= self.size:
            i = 1
            self.iterator = self.primeiroNode
            while i < position:
                if self.iterator.proxNode is not None:
                    self.iterator = self.iterator.proxNode
                    i = i + 1
            return
