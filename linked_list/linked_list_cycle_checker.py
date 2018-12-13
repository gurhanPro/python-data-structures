def linked_list_cycle_checker(node):
    m1 = node
    m2 = node
    
    while(m1 != None and m1.next != None):
        m1 = m1.next.next
        m2 = m2.next
        
        if m1 == m2:
            return True
        
    return False

def reverse(head):
    current = head
    prev = None
    next = None
    
    while current:
        next = current.next
        current.next = prev
        
        prev = current
        current = next
    return prev.value
