def p(g):
    # brute-force tile size using dict
    for q in range(1,30):
        for p in range(1,30):
            d={(y%q,x%p):v for y,r in enumerate(g)for x,v in enumerate(r)if v}
            if all(d.get((y%q,x%p))==v for y,r in enumerate(g)for x,v in enumerate(r)if v):
                return[[d.get((y%q,x%p),0)for x in range(29)]for y in range(29)]
