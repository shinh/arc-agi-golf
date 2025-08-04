def p(g):
    cnt=Counter()
    for r in g:cnt.update(r)
    bg=cnt.most_common(1)[0][0]
    for c in cnt:
        if c==bg:continue
        pos=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        rows=[i for i,j in pos];cols=[j for i,j in pos]
        if len(pos)!=(max(rows)-min(rows)+1)*(max(cols)-min(cols)+1):return [[c]]
