def p(g,u=enumerate):# fill zeros from repeating block
    j=i=1
    while any(a*b*(a-b)for r in g for a,b in zip(r,r[j:])):j+=1
    while any(a*b*(a-b)for r in zip(*g)for a,b in zip(r,r[i:])):i+=1
    d={(y%i,x%j):v for y,r in u(g)for x,v in u(r)if v};return[[v or d[y%i,x%j]for x,v in u(r)]for y,r in u(g)]
