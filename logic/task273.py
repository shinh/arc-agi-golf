def p(g):
    # fill rectangles enclosed by 4s
    rows=[{i for i in range(10)if r[i]==4}for r in g]
    for y2 in range(10):
        for y1 in range(y2):
            for a in rows[y1]&rows[y2]:
                for b in rows[y1]&rows[y2]:
                    for r in g[y1+1:y2]:r[a+1:b]=[2]*(b-a-1)
    return g
