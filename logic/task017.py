def p(g,u=enumerate):
    # fill zeros from repeating block
    f=lambda a,b:a==b or a*b<1
    for j in range(1,len(g[0])+1):
        if all(f(a,b)for r in g for a,b in zip(r,r[j:])):break
    for i in range(1,len(g)+1):
        if all(f(a,b)for r,s in zip(g,g[i:])for a,b in zip(r,s)):break
    d={(y%i,x%j):v for y,r in u(g) for x,v in u(r) if v}
    return[[v or d[y%i,x%j] for x,v in u(r)]for y,r in u(g)]
