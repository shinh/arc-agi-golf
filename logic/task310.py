def p(g):
    h=len(g);w=len(g[0])
    best=None
    for c in {v for r in g for v in r}:
        pos=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==c]
        if not pos:continue
        rows=[i for i,j in pos];cols=[j for i,j in pos]
        si,ei=min(rows),max(rows);sj,ej=min(cols),max(cols)
        if ei-si<1 or ej-sj<1:continue
        border={(i,sj)for i in range(si,ei+1)}|{(i,ej)for i in range(si,ei+1)}|{(si,j)for j in range(sj,ej+1)}|{(ei,j)for j in range(sj,ej+1)}
        if set(pos)==border:
            area=(ei-si+1)*(ej-sj+1)
            if not best or area<best[0]:best=(area,si,ei,sj,ej)
    if not best:return g
    _,si,ei,sj,ej=best
    return [row[sj:ej+1] for row in g[si:ei+1]]
