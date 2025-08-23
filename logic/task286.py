# rotate & fill alternating colors

def p(g):
    for t in[sum({*sum(g,[])})]*272:g=[[a or b%8 and t-b-8 for a,b in zip(r,r[1:]+(8,))]for r in zip(*g[::-1])]
    return g
