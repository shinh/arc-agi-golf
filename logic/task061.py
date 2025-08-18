def p(g):
    # infer tile with setdefault
    for k in range(1,19):
        d={}
        if all(d.setdefault((y%k,x%k),v)==v for y,r in enumerate(g) for x,v in enumerate(r) if v):
            return[[d.get((y%k,x%k),0)for x in range(18)]for y in range(18)]
