def p(g):
    # pick dominant colors for rows or cols
    return([[max(r,key=r.count)]*len(r)for r in g],[[max(c,key=c.count)for c in zip(*g)]]*len(g))[sum(map(len,map(set,zip(*g))))<sum(map(len,map(set,g)))]
