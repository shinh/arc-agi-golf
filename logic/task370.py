def p(g):# copy shape along best diagonal
    h=len(g);w=len(g[0]);bg=g[0][0];cols={}
    for n,v in enumerate(sum(g,[])):
        if v-bg:cols[v]=cols.get(v,set())|{divmod(n,w)}
    (_,S),(c2,B)=sorted(cols.items(),key=lambda t:len(t[1]))[-1:-3:-1];s=1
    while {(i+s,j+s)for i,j in S}&S:s+=1
    d=max((-s,-s),(-s,s),(s,-s),(s,s),key=lambda d:len({(i+d[0],j+d[1])for i,j in S}&B))
    for x,y in S:
        while h>(x:=x+d[0])>=0<=(y:=y+d[1])<w:g[x][y]=c2
    return g
