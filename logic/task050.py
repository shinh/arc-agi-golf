def p(g):
    # fill gaps between two 8s horizontally then vertically
    for _ in 0,1:
        for r in g:
            try:a=r.index(8);b=len(r)+~r[::-1].index(8);r[a+1:b]=[v or 3 for v in r[a+1:b]]
            except:0
        g=[*map(list,zip(*g))]
    return g
