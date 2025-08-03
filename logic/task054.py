def p(g):
    h=[r[:]for r in g]
    H=len(g);W=len(g[0]);b=g[0][0]
    v=[[0]*W for _ in g];R=[]
    for y in range(H):
        for x in range(W):
            if g[y][x]!=b and not v[y][x]:
                c=g[y][x];q=[(y,x)];v[y][x]=1;C=[]
                while q:
                    Y,X=q.pop();C.append((Y,X))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=Y+dy,X+dx
                        if 0<=ny<H and 0<=nx<W and g[ny][nx]==c and not v[ny][nx]:
                            v[ny][nx]=1;q.append((ny,nx))
                ys=[p[0] for p in C];xs=[p[1] for p in C]
                y0,y1,x0,x1=min(ys),max(ys),min(xs),max(xs)
                if len(C)>20 and (y1-y0+1)*(x1-x0+1)-len(C)<5:R.append((y0,y1,x0,x1,c))
    m=[[-1]*W for _ in g]
    for i,(y0,y1,x0,x1,c) in enumerate(R):
        for y in range(y0,y1+1):
            for x in range(x0,x1+1):m[y][x]=i
    P=[(y,x) for y in range(H) for x in range(W) if g[y][x]!=b and m[y][x]<0]
    my=min(y for y,x in P);My=max(y for y,x in P);mx=min(x for y,x in P);Mx=max(x for y,x in P)
    pat=[[b]*(Mx-mx+1) for _ in range(My-my+1)]
    for y,x in P:pat[y-my][x-mx]=g[y][x]
    for y,x in P:h[y][x]=b
    cy,cx=(len(pat)-1)//2,(len(pat[0])-1)//2;cen=pat[cy][cx]
    ph,pw=len(pat),len(pat[0])
    def arm(dy,dx):
        y,x=cy+dy,cx+dx
        if not(0<=y<ph and 0<=x<pw) or pat[y][x]==b:return b,0
        c=pat[y][x];n=1
        while 0<=y+dy<ph and 0<=x+dx<pw and pat[y+dy][x+dx]==c:
            y+=dy;x+=dx;n+=1
        return c,n
    u,nu=arm(-1,0);d,nd=arm(1,0);l,nl=arm(0,-1);r,nr=arm(0,1)
    dots=[]
    for i,(y0,y1,x0,x1,c) in enumerate(R):
        for y in range(y0,y1+1):
            for x in range(x0,x1+1):
                if g[y][x]!=c:dots.append((i,y,x))
    for i,y,x in dots:
        y0,y1,x0,x1,c=R[i]
        for dy,row in enumerate(pat):
            ty=y-cy+dy
            if y0<=ty<=y1:
                for dx,val in enumerate(row):
                    tx=x-cx+dx
                    if x0<=tx<=x1:h[ty][tx]=c if val==b else val
        if nu>1:
            for Y in range(y0,y):h[Y][x]=u
        if nd>1:
            for Y in range(y+1,y1+1):h[Y][x]=d
        if nl>1:
            for X in range(x0,x):h[y][X]=l
        if nr>1:
            for X in range(x+1,x1+1):h[y][X]=r
        h[y][x]=cen
    return h
