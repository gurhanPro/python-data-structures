## pair_sum([1,3,2,2],4)
def pair_sum(lis,k):
    """ returns a unique pairs that add up to k
      arguments:
    list: the list to checked
    k:    the number the pairs must sum to 
    """
    re = []
    for l in lis:
        for j in lis:
            if l + j == k:
                
                if l in re:
                    pass
                else:
                    re.append(j)
                    re.append(l)
    st = ""
    for i in range(0,len(re)-1,2):
        st += '({}, {})   '.format(re[i],re[i+1])
    return st



##################################################333
########## another way to do it using sets

def psum(arr,k):
    
    if len(arr)<2:
        return null
   
    seen = set()
    
    output = set()
    for num in arr:
        target  = k-num
        if target not in seen:
            seen.add(num)
        else:
            
            output.add((num,target))
    
   
    return  print(output)
