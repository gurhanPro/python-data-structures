# ignore cases and spaces
def anagram_check(s,ss):
""" This method checks if two strings are anagrams of each other We ignore cases and trim spaces
Argument: s,ss are the two strings being checked for anagram
returns boolean

question: Given two strings, check if they are anagrams
"""
    s1 = sorted(s.replace(" ","").lower())
    s2 = sorted(ss.replace(" ","").lower())
    if len(s1) != len(s2):
        return False
    else:
        s1 = sorted(s.replace(" ","").lower())
        s2 = sorted(ss.replace(" ","").lower())
        if s1!=s2:
            return False
        else:
#             print(s1)
#             print(s2)
            return True
    return True
