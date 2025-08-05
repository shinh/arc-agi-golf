def p(g):
    h=len(g);w=len(g[0])
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:d.setdefault(v,set()).add((y,x))
    for c,s in d.items():
        ys,xs=zip(*s)
        if len(s)==(max(ys)-min(ys)+1)*(max(xs)-min(xs)+1):rc=s;R=c
        else:sh=s;S=c
    v=lambda s:{(i,(m:=min(j for _,j in s)+max(j for _,j in s))-j)for i,j in s}
    h_=lambda s:{((m:=min(i for i,_ in s)+max(i for i,_ in s))-i,j)for i,j in s}
    u=rc|sh;ys,xs=zip(*u)
    m=max((max(ys)-min(ys)+1)//2+1,(max(xs)-min(xs)+1)//2+1)
    best=set();sc=-1
    for P in(v(sh),h_(sh)):
        for dj in range(-m,m+1):
            for di in range(-m,m+1):
                s={(i+di,j+dj)for i,j in P}
                if all((0<=i<h and 0<=j<w and g[i][j]) or not(0<=i<h and 0<=j<w) for i,j in s):
                    t=len(s&sh)
                    if t>sc:sc=t;best=s
    for i,j in rc:g[i][j]=0
    for i,j in best:g[i][j]=S
    return g
