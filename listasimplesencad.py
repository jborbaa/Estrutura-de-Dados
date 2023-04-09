from listaduplaencad import ListaDuplaEncadeada


class ListNo:
   

    def __init__(self, data, listaDE: ListaDuplaEncadeada, nextNo=None):
        self.data = data
        self.listaDE = listaDE
        self.nextNo = nextNo


class ListaSimplesEncadeada:


    def __init__(self, firstNo=None):
        self.firstNo = firstNo
        self.lastNo = firstNo
        self.iterator = firstNo
        if firstNo:
            self.size = 1
        else:
            self.size = 0

    def addNo(self, data: any, listaDE: ListaDuplaEncadeada):
       

        newNo = ListNo(data, listaDE)
        newNo.nextNo = None
        if self.size == 0:
            self.iterator = newNo
            self.firstNo = newNo
            self.lastNo = newNo
        elif self.iterator == self.lastNo:
            self.lastNo.nextNo = newNo
            self.iterator = newNo
            self.lastNo = newNo
        else:
            newNo.nextNo = self.iterator.nextNo
            self.iterator.nextNo = newNo
            self.iterator = newNo
        
        if listaDE != None:
            newNo.listaDE = listaDE
        self.size += 1
        return True


    def insNo(self, data, ListaDE: ListaDuplaEncadeada):
       
        newNo = ListNo(data, ListaDE)
        newNo.nextNo = None
        if self.size == 0:
            self.iterator = newNo
            self.firstNo = newNo
            self.lastNo = newNo
        elif self.iterator == self.firstNo:
            newNo.nextNo = self.firstNo
            self.firstNode = newNo
            self.iterator = newNo
        else:
            currentNo = self.firstNo
            while currentNo.nextNo != self.iterator:
                currentNo = currentNode.nextNo
            newNo.nextNo = self.iterator
            currentNode.nextNo = newNo
            self.iterator = newNo
        self.size += 1
        return True


    def elimNo(self):
      
        if self.iterator == self.firstNo:
            if self.lastNo == self.firstNo:
                self.lastNo = None
                self.firstNo = None
                self.iterator = None
            else:
                self.firstNo = self.firstNo.nextNo
                self.iterator.nextNo = None
                self.iterator = self.firstNo
        else:
            currentNo = self.firstNo
            while currentNo.nextNo != self.iterator:
                currentNo = currentNode.nextNo
            if self.iterator == self.lastNo:
                self.lastNo = currentNo
                self.iterator.nextNo = None
                self.iterator = None
                currentNo.nextNo = None
            else:
                currentNo.nextNo = self.iterator.nextNo
                currentNo = self.iterator
                self.iterator = self.iterator.nextNo
                currentNode.nextNo = None
        self.size = self.size - 1
        return True

    
    def last_No(self):
     
        self.iterator = self.lastNo
        return True


    def first_No(self):
      
        self.iterator = self.firstNo
        return True

    def nextNo(self):
      
        if self.iterator:
            self.iterator = self.iterator.nextNo
        return True


    def posNo(self, position: int):
      
        if position > 0 and position <= self.size:
            i = 1
            self.iterator = self.firstNo
            while i < position:
                if self.iterator.nextNo is not None:
                    self.iterator = self.iterator.nextNo
                    i = i + 1
            return