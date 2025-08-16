def p(g):
 # merge blocks separated by empty rows/cols, keep first colors
 r=range;n,m=len(g),len(g[0]);b=[-1]+[i for i in r(n)if sum(g[i])<1]+[n];c=[-1]+[j for j in r(m)if sum(k[j]for k in g)<1]+[m];return [t for a,b in zip(b,b[1:]) if (t:=[v for c,d in zip(c,c[1:]) if (v:=next((g[x][y]for x in r(a+1,b)for y in r(c+1,d)if g[x][y]),0))])]
