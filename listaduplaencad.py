class No:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class ListaDuplaEncadeada:

    def __init__(self, firstNo=None):
        self.firstNo = firstNo
        self.lastNode = firstNo
        self.iterator = firstNo
        self.size = 0 if firstNo is None else 1
        
        
    def elimNo(self):
      
        if self.iterator is not None:
            if self.iterator.prev is not None:
                self.iterator.prev.next = self.iterator.next
            else:
                self.firstNo = self.iterator.next
            if self.iterator.next is not None:
                self.iterator.next.prev = self.iterator.prev
            else:
                self.lastNo = self.iterator.prev
            self.iterator = self.iterator.next
            self.size -= 1   

    def addNo(self, data: any):
    
        newNo = No(data)
        if self.iterator is None:
            self.iterator = newNo
        if self.firstNo is None:
            self.firstNo = newNo
            self.lastNo = newNo
        else:
            newNo.prev = self.iterator
            newNo.next = self.iterator.next
            if self.iterator.next is not None:
                self.iterator.next.prev = newNo
            else:
                self.lastNode = newNo
            self.iterator.next = newNo
        self.size += 1         

    def insNode(self, data: any):
        newNo = No(data)
        if self.iterator is None:
            self.iterator = newNo
        if self.firstNo is None:
            self.firstNo = newNo
            self.lastNo = newNo
        else:
            newNo.prev = self.iterator.prev
            newNo.next = self.iterator
            if self.iterator.prev is not None:
                self.iterator.prev.next = newNo
            else:
                self.firstNo = newNo
            self.iterator.prev = newNo
        self.size += 1

    

    def first_No(self):

        self.iterator = self.firstNo



    def last_No(self):
        self.iterator = self.lastNo

    

    def anttNo(self):
    
        if self.iterator is not None:
            self.iterator = self.iterator.prev
            if self.iterator is None:
                return True
        return False
    def posNo(self, position: int):
        
        if position <= 1:
            self.first_No()
        elif position >= self.size:
            self.last_No()
        else:
            currentPos = 1
            currentNo = self.firstNo
            while currentPos < position and currentNo is not None:
                currentNo = currentNo.next
                currentPos += 1
            self.iterator = currentNo
        if self.iterator is None:
            return True
        return False

    def nextNo(self):
     
        if self.iterator is not None:
            self.iterator = self.iterator.next
            if self.iterator is None:
                return True
        return False   


    def undefinedIterator(self):
      
        return self.iterator is None