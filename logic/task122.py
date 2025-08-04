def p(g):
    h=len(g);w=len(g[0])
    col={}
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            col.setdefault(v,[]).append((i,j))
    def box(s):
        rs=[i for i,j in s];cs=[j for i,j in s];return min(rs),max(rs),min(cs),max(cs)
    bg=max(col,key=lambda c:(lambda t,b,l,r:(b-t+1)*(r-l+1))(*box(col[c])))
    colors=[c for c in col if c!=bg]
    def comps(c):
        pts=set(col[c]);d=[]
        while pts:
            st=[pts.pop()];s={st[0]}
            while st:
                x,y=st.pop()
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    p=(x+dx,y+dy)
                    if p in pts:pts.remove(p);st.append(p);s.add(p)
            d.append(s)
        return d
    comp={c:comps(c) for c in colors}
    c1=min(colors,key=lambda c:len(comp[c]));colors.remove(c1);c2=colors[0]
    patch=set(col[c1])
    objs=comp[c2]
    def bb(o):
        t,b,l,r=box(o);return t,b,l,r
    top=min(objs,key=lambda o:bb(o)[0]+bb(o)[2])
    other=min([o for o in objs if o!=top],key=lambda o:min(abs(a-b)+abs(c-d) for a,c in top for b,d in o))
    t1,b1,l1,r1=bb(top);t2,b2,l2,r2=bb(other)
    di=0 if len({bb(o)[0] for o in objs})==1 else max(b2-b1,t2-t1)
    dj=0 if len({bb(o)[2] for o in objs})==1 else max(r2-r1,l2-l1)
    def shift(s,di,dj):
        return {(i+di,j+dj) for i,j in s}
    P=shift(patch,di,dj)
    def del_ul(s):
        t,b,l,r=box(s)
        for i in range(t,b+1):
            for j in range(l,r+1):
                if (i,j)not in s:return i,j
    du=del_ul(P)
    def hmir(s):
        t,b,l,r=box(s);return {(t+b-i,j) for i,j in s}
    def vmir(s):
        t,b,l,r=box(s);return {(i,l+r-j) for i,j in s}
    def align(s):
        u=del_ul(s);di,dj=du[0]-u[0],du[1]-u[1];return shift(s,di,dj)
    P1=P|align(hmir(P))
    P2=align(vmir(P1))
    P=P1|P2
    res=[r[:] for r in g]
    for i,j in col[c1]:res[i][j]=bg
    for i,j in P:
        if 0<=i<h and 0<=j<w:res[i][j]=c1
    return res
