def p(g):
    g=[r[:]for r in g];h=len(g);w=len(g[0])
    bg=max(range(10),key=lambda c:sum(r.count(c)for r in g))
    fg={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v!=bg}
    t=min(i for i,_ in fg);b=max(i for i,_ in fg);l=min(j for _,j in fg);R=max(j for _,j in fg)
    s={(i,j)for j in range(l,R+1)for i in(t,b)if(i,j)not in fg}|{(i,j)for i in range(t,b+1)for j in(l,R)if(i,j)not in fg}
    for i in range(t,b+1):
     for j in range(l,R+1):
      if(i,j)not in fg:g[i][j]=4
    if s:
     si,sj=zip(*s)
     T=min(si)==t;L=min(sj)==l;B=max(si)==b
     ul=(min(si),min(sj));ur=(min(si),max(sj));ll=(max(si),min(sj));lr=(max(si),max(sj))
     a=ur if T else ul if L else ll if B else lr
     b=ul if T else ll if L else lr if B else ur
     if T:d1,d2,d3=(-1,1),(-1,-1),(-1,0)
     elif L:d1,d2,d3=(-1,-1),(1,-1),(0,-1)
     elif B:d1,d2,d3=(1,-1),(1,1),(1,0)
     else:d1,d2,d3=(1,1),(-1,1),(0,1)
     def sH(p,d):
      i,j=p;di,dj=d
      while 0<=i<h and 0<=j<w:g[i][j]=4;i+=di;j+=dj
     sH(a,d1);sH(b,d2)
     for p in s:sH(p,d3)
    return g
