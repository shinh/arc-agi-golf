def p(g):
    # find smallest isolated color and crop
    d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:
                t=d.setdefault(v,[0,y,x,y,x]);t[0]+=1;t[1]=min(t[1],y);t[2]=min(t[2],x);t[3]=max(t[3],y);t[4]=max(t[4],x)
    _,k,y0,x0,y1,x1=min((n,k,y0,x0,y1,x1)for k,(n,y0,x0,y1,x1)in d.items()if all(v in(0,k)for r in g[y0:y1+1]for v in r[x0:x1+1]))
    return[[k*(v==k)for v in r[x0:x1+1]]for r in g[y0:y1+1]]
