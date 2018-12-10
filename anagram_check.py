# ignore cases and spaces
def anagram_check(s,ss):
""" This method checks if two strings are anagrams of each other We ignore cases and trim spaces
Argument: s,ss are the two strings being checked for anagram
returns boolean

question: Given two strings, check if they are anagrams
"""
    s1 = sorted(s.replace(" ","").lower()) # lowering letters, triming spaces and sorting the string
    s2 = sorted(ss.replace(" ","").lower())
            
    return s1!=s2 # returns true if the strings are the same else false


########################################
#longer version
# using dictionary 
# for every unique character in the string we will add it to dictionary and the key will be the number of times it appears

def anagram(s,ss):
    
    s = s.replace(" ","").lower()
    ss = ss.replace(" ","").lower()
    if len(s) != len(ss):
        return False
    dic = {}
    for l in s:
        if l in dic:
            dic[l]+=1
        else:
            dic[l] = 1
    print(dic)        
    for l in ss:
        if l in dic:
            dic[l]-= 1
        else:
            dic[l] = 1
            
    for i in dic:
        if dic[i]!=0:
            return False
        else:
            return True
