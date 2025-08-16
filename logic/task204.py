# flood fill using rot90 so we only flow to the right
def p(g):
    for _ in[0]*80:
        g=[[[a,2][a<1<b]for a,b in zip(r,[*r[1:],2])]for r in zip(*g[::-1])]
    for r in g:
        s=-1
        for x,c in enumerate(r):
            if c==0:
                if s<0:
                    r[s:=x]=2
                r[s:x+1]=[9-r[s]]*(x+1-s)
            if c==1:
                s=-1
            if c==2:
                r[x]=0
    return g
