def p(g):
    # tile period
    s=range(29);r=range(1,30)
    return next([[d.get((y%q,x%p),0)for x in s]for y in s]for q in r for p in r if(d:={})or all(d.setdefault((y%q,x%p),v)==v for y in s for x in s if(v:=g[y][x])))
