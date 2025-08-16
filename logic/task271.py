def p(g):# pick 3x3 with most 1s then 8s
    R=range(7);m,b,n=max((sum(9*(v==1)+v//8for r in g[y:y+3]for v in r[x:x+3]),y,x)for y in R for x in R);return[r[n:n+3]for r in g[b:b+3]]
