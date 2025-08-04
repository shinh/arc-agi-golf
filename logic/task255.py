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
        cy=(T+B)//2;cx=(L+R)//2
        for c in range(L,R+1):r[cy][c]=3
        for r0 in range(T,B+1):r[r0][cx]=3
    return r

# TODO: refine cross dimensions to match task description precisely
