def permute(s):
    """
        given a string return all permutations of that string using recursion
        e.g permute("abc") =    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """ #abc = abc, acb, 
    out = []
    
    #Base Case
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]
    return out
