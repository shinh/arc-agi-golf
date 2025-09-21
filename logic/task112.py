def p(g):# mirror colors at 2x2 core
    w=len(g[0]);f=sum(g,[]);s,t=next((i//w*2+1,i%w*2+1)for i,v in enumerate(f)if v and f.count(v)==4)
    for i,c in enumerate(f):
        if c:y=i//w;i%=w;g[y][i]=g[y][t-i]=g[s-y][i]=g[s-y][t-i]=c
    return g
