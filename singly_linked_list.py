class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None    
        
        
        
        
a = Node(1)
b = Node(2)
c = Node("three")        


a.nextNode = b
b.nextNode = c
