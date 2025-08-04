def p(g):
    col={c for r in g for c in r}
    bg=max(col,key=lambda c:sum(r.count(c) for r in g))
    pats=[];S=0
    for v in col-{bg}:
        ys=[];xs=[]
        for y,r in enumerate(g):
            for x,c in enumerate(r):
                if c==v:ys+=[y];xs+=[x]
        y1,y2=min(ys),max(ys);x1,x2=min(xs),max(xs)
        sub=[[c if c==v else bg for c in r[x1:x2+1]] for r in g[y1:y2+1]]
        h=len(sub);w=len(sub[0]);s=0
        for r in sub+list(zip(*sub)):
            if r.count(v)==len(r):s=max(s,len(r))
            else:
                idx=[i for i,c in enumerate(r) if c==v]
                if idx:
                    a=b=idx[0];R=[]
                    for i in idx[1:]:
                        if i==b+1:b=i
                        else:R+=[(a,b)];a=b=i
                    R+=[(a,b)]
                    if len(R)==2:
                        l1=R[0][1]-R[0][0]+1
                        l2=R[1][1]-R[1][0]+1
                        s=max(s,max(l1,l2)*2+R[1][0]-R[0][1]-1)
        if not s:s=max(h,w)
        pts=[(y,x) for y in range(h) for x in range(w) if sub[y][x]==v]
        ys=[y for y,x in pts]; xs=[x for y,x in pts]
        oy=0 if s==h else s-h if h-1 in ys else 0 if 0 in ys else (s-h)//2
        ox=0 if s==w else s-w if w-1 in xs else 0 if 0 in xs else (s-w)//2
        t=[[bg]*s for _ in range(s)]
        for i,row in enumerate(sub): t[oy+i][ox:ox+w]=row
        for y in range(s):
            for x in range(s):
                if t[y][x]==v:t[-1-y][-1-x]=v
        pats+=[(s,t)]
        S=max(S,s)
    out=[[bg]*S for _ in range(S)]
    for s,t in sorted(pats,reverse=True):
        o=(S-s)//2
        for y in range(s):
            for x in range(s):
                c=t[y][x]
                if c!=bg:out[o+y][o+x]=c
    return out
