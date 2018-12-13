class DoublyLinkedList(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
   
   
d = DoublyLinkedList(5)
e = DoublyLinkedList('e')
f = DoublyLinkedList('ef')
g = DoublyLinkedList('gii')


d.next = e
e.prev=d
e.next = f
f.prev=e
f.next=g
g.prev =f
