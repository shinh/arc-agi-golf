def p(g):
    d={}
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v:
                if v in d:
                    a=d[v];a[0]=min(a[0],y);a[1]=max(a[1],y);a[2]=min(a[2],x);a[3]=max(a[3],x)
                else:
                    d[v]=[y,y,x,x]
    k=max(d.items(), key=lambda kv:((kv[1][1]-kv[1][0]+1)*(kv[1][3]-kv[1][2]+1),kv[1][0],-kv[1][2]))[0]
    return [[k]*2 for _ in range(2)]
