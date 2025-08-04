def p(g):
    l=[r[:2]for r in g];r=[r[3:]for r in g]
    q=[tuple(map(tuple,x))for x in(l[:2],r[:2],l[3:],r[3:])]
    return[list(r)for r in min(q,key=q.count)]
