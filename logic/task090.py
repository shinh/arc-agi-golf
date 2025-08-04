def p(g):
    h=len(g);w=len(g[0])
    ps=[[0]*(w+1)for _ in range(h+1)]
    for i,r in enumerate(g):
        s=0;row=ps[i+1];pr=ps[i]
        for j,v in enumerate(r):
            s+=v<1
            row[j+1]=pr[j+1]+s
    mx=0;R=[]
    for a in range(h):
        for b in range(w):
            for c in range(a+1,h):
                for d in range(b+1,w):
                    area=(c-a+1)*(d-b+1)
                    if area>mx and ps[c+1][d+1]-ps[a][d+1]-ps[c+1][b]+ps[a][b]==area:
                        mx=area;R=[(a,b,c,d)]
                    elif area==mx and mx and ps[c+1][d+1]-ps[a][d+1]-ps[c+1][b]+ps[a][b]==area:
                        R.append((a,b,c,d))
    for a,b,c,d in R:
        for i in range(a,c+1):
            for j in range(b,d+1):g[i][j]=6
    return g
