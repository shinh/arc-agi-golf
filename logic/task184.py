def p(g):
 # merge blocks separated by empty rows/cols, keep first colors
 R=range
 n,m=len(g),len(g[0])
 r=[-1]+[i for i in R(n)if not any(g[i])]+[n]
 c=[-1]+[j for j in R(m)if not any(g[i][j]for i in R(n))]+[m]
 return [t for a,b in zip(r,r[1:]) if (t:=[v for c,d in zip(c,c[1:]) if (v:=next((g[x][y]for x in R(a+1,b)for y in R(c+1,d)if g[x][y]),0))])]
