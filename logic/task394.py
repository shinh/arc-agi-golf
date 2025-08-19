# 240
def p(g):
    # detect repeat and fill zero box
    p=1
    for o in"00":
        for r in g:
            if len({*r})>1 and 0 not in r:
                for p in range(1,9):
                    if all(c==r[x%p]for x,c in enumerate(r)):
                        break
                break
        g=[*map(list,zip(*g))]
    return[[g[y%p][x%p]or g[y%p+p][x%p+p]for x,c in enumerate(r)if c<1]for y,r in enumerate(g)if 0in r]
