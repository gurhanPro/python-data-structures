class BinHeap():
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self, i):
        i=1
        while i // 2 > 0 :
                   
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def minChild(self,i):
        if i*2 + 1 > self.currentSize: # checks if there is only one child
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1
            
    def percDown(self,i):
        while i *2 + 1 < self.currentSize: 
            mc = self.minChild(i)
            
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
            
        
    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retVal
    
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        
        while i > 0:
            self.percDown(i)
            i = i-1   
    
    def size(self):
        return self.currentSize
    
    
