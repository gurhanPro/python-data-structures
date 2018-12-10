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
                    
    return re
