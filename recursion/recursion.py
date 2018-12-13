# n = 4! = 4*3*2*1
def fact(n):
    
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
        
        
        
        
# n = 4 = 4 + 3 + 2 + 1        
def sumrec(n):
    if n == 0:
        return 0
    else:
        return n + sumrec(n-1)
        
 # n = 5321 = 5+3+2+1 = 11
 
 
 def sum_digits_rec(n):
    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_digits_rec(n//10)
        
        
def word_phrase_rec(phrase,word_list,output=None):
    
    if output is None:
        output = []
    
    for word in word_list:
        if phrase.startswith(word):
            output.append(word)
            
            return word_phrase_rec(phrase[len(word):], word_list, output)
    return output
    
    #jk('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
    #['i', 'love', 'dogs', 'John']
