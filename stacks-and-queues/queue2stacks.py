class Queeu2stacks(object):
    """ this class implements queue using two stacks
        
    """
    def __init__(self):
        
        self.instack = []
        self.outstack = []
    
    def enq(self,item):
        self.instack.append(item)
    
    def deq(self):
        if not self.outstack:
            while(self.instack):
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
    
    def p(self):
        print('instack: {}'.format(self.instack))
        print('outstack: {}'.format(self.outstack))
        
