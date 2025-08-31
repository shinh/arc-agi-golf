# recolor rectangular loops
def p(g):
    for t in range(144):
        g=[[[c,[2,3,0][p:=t//48]][c==p and(n%3==[2,0,0][p] or p==2)]for c,n in zip(r,[*r[1:],2])]for r in zip(*g[::-1])]
    return g
