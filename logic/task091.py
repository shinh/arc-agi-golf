def p(g):
    y=[];x=[]
    for j,r in enumerate(g):
        for i,v in enumerate(r):
            if v==5:y+=j,;x+=i,
    a=max(0,min(y)-1);b=min(len(g),max(y)+2);c=min(x);d=max(x)+1
    return [r[c:d] for r in g[a:b]]
