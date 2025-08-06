def p(g):
    h=len(g);w=len(g[0]);D=1,0,-1,0,1
    v=[[0]*w for _ in g];s=0
    for y in range(h):
        for x in range(w):
            if g[y][x]<1 and not v[y][x]:
                q=[y,x];v[y][x]=1;n=0;a=h;c=w;b=e=0
                while q:
                    j=q.pop();i=q.pop();n+=1;a=min(a,i);c=min(c,j);b=max(b,i);e=max(e,j)
                    for k in range(4):
                        ni=i+D[k];nj=j+D[k+1]
                        if 0<=ni<h and 0<=nj<w and g[ni][nj]<1 and not v[ni][nj]:
                            v[ni][nj]=1;q+=ni,nj
                if n==(b-a+1)*(e-c+1) and n>s:s=n;A=a;B=b;C=c;E=e
    P=[r[C-1:E+2]for r in g[A-1:B+2]]
    H=B-A+3;W=E-C+3
    E=[(g[y][x],y,x)for y in range(h)for x in range(w)if g[y][x] and not(A-1<=y<=B+1 and C-1<=x<=E+1)]
    C=[(k,y,x)for y,r in enumerate(P)for x,k in enumerate(r)if k]
    if E:
        I=min(y for _,y,_ in E);J=min(x for _,_,x in E)
        for k,y,x in E:
            y-=I-1;x-=J-1
            if 0<=y<H and 0<=x<W:
                m=99;c=k
                for l,i,j in C:
                    d=abs(y-i)+abs(x-j)
                    if d<m:m=d;c=l
                    elif d==m and l!=c:c=k
                P[y][x]=c
    return P
