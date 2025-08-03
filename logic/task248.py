def p(g):
    h=len(g);w=len(g[0])
    x=g[-1].index(1);d=1;seq=[]
    for _ in range(h):
        seq.append(x)
        if x+d<0 or x+d>=w:d*=-1
        x+=d
    o=[[0]*w for _ in g]
    for y,x in enumerate(seq[::-1]):o[y][x]=1
    return o
