def p(g):
    h, w = len(g), len(g[0])
    rows = [i for i, r in enumerate(g) if r.count(r[0]) == w]
    cols = [j for j in range(w) if len({g[i][j] for i in range(h)}) == 1]
    fc = g[rows[0]][0] if rows else g[0][cols[0]]
    cnt = {}
    for r in g:
        for v in r:
            if v != fc:
                cnt[v] = cnt.get(v, 0) + 1
    if not cnt:
        return g
    bg = max(cnt, key=cnt.get)
    out = [r[:] for r in g]
    for c in cnt:
        if c == bg:
            continue
        pts = [(i, j) for i in range(h) for j in range(w) if g[i][j] == c]
        n = len(pts)
        for a in range(n):
            i1, j1 = pts[a]
            for b in range(a + 1, n):
                i2, j2 = pts[b]
                if i1 == i2 and (j1 + j2) % 2 == 0:
                    out[i1][(j1 + j2) // 2] = c
                elif j1 == j2 and (i1 + i2) % 2 == 0:
                    out[(i1 + i2) // 2][j1] = c
    return out

