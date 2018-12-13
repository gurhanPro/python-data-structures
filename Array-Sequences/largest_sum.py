	def maxsum(arr):
    current_sum = largest_sum = arr[0]

    for i in arr[1:]:
        if current_sum + i > i:
            current_sum = current_sum + i
        else:
            current_sum = i
        
        if current_sum > largest_sum :
            largest_sum = current_sum
            
                  
        
    print('final current_sum {}'.format(current_sum))
    print('final ls {}'.format(largest_sum))
    
    #     for i in arr[1:]:
#         current_sum = max(current_sum+i, i)
#         largest_sum = max(current_sum, largest_sum)
#     return largest_sum
    
    return largest_sum
