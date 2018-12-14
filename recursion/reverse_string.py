def rev(st, out=""):
    
    if len(st)==0:
        return out
    else:
        out = out + str(st[-1])
        return rev(st[:-1], out)
    
    return out
def rev2(st):
    if len(st)==1:
        return s
    print(st)
    return rev(st[1:]) + s[0]
