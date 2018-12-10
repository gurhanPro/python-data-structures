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
