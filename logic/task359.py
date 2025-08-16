def p(g):
    # pick dominant colors for rows or cols
    if sum(len({*c})for c in zip(*g))<sum(len({*r})for r in g):
        return[[max(c,key=c.count)for c in zip(*g)]]*len(g)
    return[[max(r,key=r.count)]*len(r)for r in g]
