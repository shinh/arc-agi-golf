# rotate & fill alternating colors

def p(g):
    t=sum({*sum(g,[])}-{0,8})
    for _ in[0]*272:g=[[a or b%8 and t-b for a,b in zip(r,r[1:]+(8,))]for r in zip(*g[::-1])]
    return g
