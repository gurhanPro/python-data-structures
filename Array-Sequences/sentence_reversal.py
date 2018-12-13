def rev_sent(str):
    str_list = str.split() # splitting the string via space and putting it into array
    return print(' '.join(str_list[::-1])) # returns reversed array which is converted back to string joined by spaces
