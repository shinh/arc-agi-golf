def p(g):
    h=len(g);w=len(g[0]);b=0
    for t in range(h):
        m=[1]*w
        for btm in range(t,h):
            for c in range(w):m[c]&=g[btm][c]<1
            k=0
            for c in range(w):
                if m[c]:
                    k+=1;a=k*(btm-t+1)
                    if a>b:b=a;T,B,L,R=t,btm,c-k+1,c
                else:k=0
    r=[r[:] for r in g]
    if b:
        ys=[(T+B)//2];xs=[(L+R)//2]
        if (B-T)%2==1:ys+=[ys[0]+1]
        if (R-L)%2==1:xs+=[xs[0]+1]
        for y in ys:
            for c in range(L,R+1):r[y][c]=3
        for x in xs:
            for y in range(T,B+1):r[y][x]=3
    return r

# TODO: remaining examples show wider or offset bands; derive bar thickness and
# placement from task description rather than assuming at most two central lines.
