def p(g):
    h=w=16
    coords = [(i, j) for i, r in enumerate(g) for j, v in enumerate(r) if v == 3]
    g = [[-1 if v == 3 else v for v in r] for r in g]
    r = [[max(g[i][j], g[j][i], g[h-1-i][j], g[i][w-1-j], g[h-1-i][w-1-j], g[w-1-j][h-1-i], g[j][w-1-i], g[w-1-j][i]) for j in range(w)] for i in range(h)]
    a = min(i for i, _ in coords); b = max(i for i, _ in coords)
    c = min(j for _, j in coords); d = max(j for _, j in coords)
    return [row[c:d+1] for row in r[a:b+1]]

