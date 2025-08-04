from collections import Counter


def p(g):
    h, w = len(g), len(g[0])
    r = sum(len(set(row)) == 1 for row in g)
    c = sum(len({g[i][j] for i in range(h)}) == 1 for j in range(w))
    if r > c:
        h2, off = h // 2, h % 2
        a, b = g[:h2], g[h2 + off :]
    else:
        w2, off = w // 2, w % 2
        a = [row[:w2] for row in g]
        b = [row[w2 + off :] for row in g]
    if len({v for row in a for v in row}) <= len({v for row in b for v in row}):
        base, other = [row[:] for row in a], b
    else:
        base, other = [row[:] for row in b], a
    bc = Counter(v for row in base for v in row).most_common(1)[0][0]

    def objs(grid):
        bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
        H, W = len(grid), len(grid[0])
        seen = set()
        out = []
        for i in range(H):
            for j in range(W):
                if grid[i][j] != bg and (i, j) not in seen:
                    q = [(i, j)]
                    comp = []
                    seen.add((i, j))
                    while q:
                        x, y = q.pop()
                        comp.append((grid[x][y], (x, y)))
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != bg and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                q.append((nx, ny))
                    out.append(comp)
        return out

    O = objs(other)
    if not O:
        return base
    oc = Counter(v for o in O for v, _ in o).most_common(1)[0][0]
    H, W = len(base), len(base[0])
    pad = [[bc] * (W + 2) for _ in range(H + 2)]
    for i, row in enumerate(base):
        for j, v in enumerate(row):
            pad[i + 1][j + 1] = v
    for obj in O:
        cells = [pos for _, pos in obj]
        mi = min(i for i, j in cells)
        mj = min(j for i, j in cells)
        ma = max(i for i, j in cells)
        mb = max(j for i, j in cells)
        pat = [(bc, (i, j)) if v == oc else (v, (i, j)) for v, (i, j) in obj]
        t, btm, l, rgt = mi - 1, ma + 1, mj - 1, mb + 1
        for i in range(t, btm + 1):
            pat.append((bc, (i, l)))
            pat.append((bc, (i, rgt)))
        for j in range(l, rgt + 1):
            pat.append((bc, (t, j)))
            pat.append((bc, (btm, j)))
        pi = min(i for _, (i, j) in pat)
        pj = min(j for _, (i, j) in pat)
        norm = [(v, (i - pi, j - pj)) for v, (i, j) in pat]
        ph = max(i for _, (i, j) in norm) + 1
        pw = max(j for _, (i, j) in norm) + 1
        occ = set()
        for si in range(len(pad) - ph + 1):
            for sj in range(len(pad[0]) - pw + 1):
                if all(pad[si + a][sj + b] == v for v, (a, b) in norm):
                    occ.add((si - 1, sj - 1))
        if not occ:
            continue
        di, dj = next(iter(occ))
        di -= pi
        dj -= pj
        for v, (i, j) in obj:
            ii, jj = i + di, j + dj
            if 0 <= ii < H and 0 <= jj < W:
                base[ii][jj] = v
    return base

