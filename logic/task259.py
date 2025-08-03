def p(g):
 y=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v-1]
 y0=min(i for i,_ in y);y1=max(i for i,_ in y)+1;x0=min(j for _,j in y);x1=max(j for _,j in y)+1
 return[[0 if c==1 else c for c in r[x0:x1]]for r in g[y0:y1]]
