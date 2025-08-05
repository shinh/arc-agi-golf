def p(g):
    h=len(g);w=len(g[0])
    f=sum(g,[])
    bg=max(f, key=f.count)
    colors=set(f)-{bg}
    objs=set()
    for c in colors:
        objs.add(frozenset((c, (i, j)) for i, r in enumerate(g) for j, v in enumerate(r) if v == c))
    def bord(obj):
        return any(i in (0, h - 1) or j in (0, w - 1) for _, (i, j) in obj)
    border = next(o for o in objs if bord(o))
    rem = objs - {border}
    tup = tuple(rem)
    first, last = tup[0], tup[-1]
    c1, cells1 = next(iter(first))[0], [p for _, p in first]
    c2, cells2 = next(iter(last))[0], [p for _, p in last]
    border = [p for _, p in border]
    def mk(cells, col):
        mi = min(i for i, _ in cells); mj = min(j for _, j in cells)
        ma = max(i for i, _ in cells); mb = max(j for _, j in cells)
        res = [[bg] * (mb - mj + 1) for _ in range(ma - mi + 1)]
        for i, j in cells:
            res[i - mi][j - mj] = col
        return res
    g1, g2, b = mk(cells1, c1), mk(cells2, c2), mk(border, c1)
    def up(G):
        return [[G[i // 2][j // 2] for j in range(len(G[0]) * 2)] for i in range(len(G) * 2)]
    def occ(G, P):
        H, W = len(P), len(P[0])
        for i in range(len(G) - H + 1):
            for j in range(len(G[0]) - W + 1):
                if all(G[i + a][j + b] == P[a][b] for a in range(H) for b in range(W)):
                    return True
        return False
    return g1 if occ(up(g1), b) else g2

