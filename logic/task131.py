def p(g):
    h=len(g);w=len(g[0]);o=[[0]*w for _ in g]
    for y,r in enumerate(g):
        if r.count(2)==w:line=y;H=1;break
    else:
        H=0;line=next(x for x in range(w)if all(r[x]==2 for r in g))
    if H:o[line]=[2]*w
    else:
        for y in range(h):o[y][line]=2
    ys=[y for y in range(h)for x in range(w)if g[y][x]==3]
    xs=[x for y in range(h)for x in range(w)if g[y][x]==3]
    if xs:
        a=min(xs);b=min(ys);A=max(xs)-a+1;B=max(ys)-b+1
        if H:
            t=line-B if max(ys)<line else line+1
            for y in range(B):
                for x in range(A):o[t+y][a+x]=g[b+y][a+x]
            r=t-1 if max(ys)<line else t+B
            if 0<=r<h:o[r]=[8]*w
        else:
            l=line-A if max(xs)<line else line+1
            for y in range(B):
                for x in range(A):o[b+y][l+x]=g[b+y][a+x]
            c=l-1 if max(xs)<line else l+A
            if 0<=c<w:
                for y in range(h):o[y][c]=8
    return o
