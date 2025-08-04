def p(g):
    h, w = len(g), len(g[0])
    seen = [[0] * w for _ in g]
    objs = []
    for i in range(h):
        for j in range(w):
            if seen[i][j]:
                continue
            col = g[i][j]
            stack = [(i, j)]
            seen[i][j] = 1
            cells = []
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and g[nx][ny] == col:
                        seen[nx][ny] = 1
                        stack.append((nx, ny))
            objs.append((col, cells))
    cnt = {}
    for c, _ in objs:
        cnt[c] = cnt.get(c, 0) + 1
    if len(cnt) == len(objs):
        area = {}
        for c, cells in objs:
            area[c] = area.get(c, 0) + len(cells)
        main = min(area, key=area.get)
    else:
        main = max(cnt, key=cnt.get)
    def sub(cells):
        mi = min(i for i, _ in cells); ma = max(i for i, _ in cells)
        mj = min(j for _, j in cells); mb = max(j for _, j in cells)
        return [row[mj:mb+1] for row in g[mi:ma+1]]
    best = None
    bestc = -1
    for c, cells in objs:
        if c == main:
            continue
        sg = sub(cells)
        ccount = sum(v == main for row in sg for v in row)
        if ccount > bestc:
            bestc = ccount
            best = sg
    freq = {}
    for row in best:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    return [[max(freq, key=freq.get)]]

