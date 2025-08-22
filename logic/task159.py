# rotate until target row then scale inside 2-frame

def p(g):
    o=g
    for _ in[0]*120:o=[*map(list,zip(*o[-2+(2 in o[-1])::-1]))]
    c,*_=({*sum(g,[])}-{0,2})
    for _ in[0]*120:g=[*zip(*g[-2+(c in g[-1])::-1])]
    n=len(o)//len(g);y=0
    for r in g:
        for _ in[0]*n:o[y:=y+1][1:-1]=[c for c in r for _ in[0]*n]
    return o

