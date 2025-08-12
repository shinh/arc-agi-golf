# rotate grid and flood fill from rare colors

def p(g):
    l=set()
    for _ in range(280):
        g=[[(l.add(b),[a,[*(l-{0,8,b}),0][0]][b not in (0,8) and a==0])[-1]for a,b in zip(r,[*r[1:],8])]for r in zip(*g[::-1])]
    return g
