# rotate until target row then scale inside 2-frame

def p(g):
    o=g
    for _ in[0]*120:o=[*zip(*o[-2+(2 in o[-1])::-1])]
    c,*_=({*sum(g,[])}-{0,2})
    for _ in[0]*120:g=[*zip(*g[-2+(c in g[-1])::-1])]
    n=len(o)//len(g);w=len(g[0])*n+2
    return [[2]*w]+[[2]+[c for c in r for _ in[0]*n]+[2]for r in g for _ in[0]*n]+[[2]*w]

