import collections
def mi(ar1,ar2):
    
    d = collections.defaultdict(int)
    for num in ar2:
        d[num] +=1
    
    for num in ar1:
        if d[num]==0:
            return num
        else:
            d[num]-=1
            
          
