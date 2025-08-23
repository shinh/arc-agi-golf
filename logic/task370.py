def p(g):# copy shape along best diagonal
    h=len(g);w=len(g[0]);cols={}
    for n,v in enumerate(sum(g,[])):v-g[0][0] and cols.setdefault(v,set()).add(divmod(n,w))
    a=sorted(cols,key=lambda k:len(cols[k]));S=cols[a[-1]];B=cols[c2:=a[-2]];s=1 # pick largest S and best c2
    while {(i+s,j+s)for i,j in S}&S:s+=1
    d=max((-s,-s),(-s,s),(s,-s),(s,s),key=lambda d:len({(i+d[0],j+d[1])for i,j in S}&B))
    for x,y in S:
        while h>(x:=x+d[0])>=0<=(y:=y+d[1])<w:g[x][y]=c2
    return g
