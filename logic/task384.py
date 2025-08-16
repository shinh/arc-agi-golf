# crop bbox of nonzeros and double size
def p(g):A=[*map(any,g)];B=[*map(any,zip(*g))];return[[x for x in r[B.index(1):len(B)-B[::-1].index(1)]for _ in(0,0)]for r in g[A.index(1):len(A)-A[::-1].index(1)]for _ in(0,0)]
