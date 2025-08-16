def p(g):
    # brute-force tile size using dict
    for q in range(1,30):
        for p in range(1,30):
            d={}
            if all(v<1 or d.setdefault((y%q,x%p),v)==v for y,r in enumerate(g)for x,v in enumerate(r)):
                return[[d.get((y%q,x%p),0)for x in range(29)]for y in range(29)]
