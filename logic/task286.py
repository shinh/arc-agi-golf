# rotate grid and flood fill from rare colors

def p(g):
    c=[0]*10
    for r in g:
        for v in r:c[v]+=1
    x,y=sorted(range(10),key=lambda k:(c[k]or 9e9,k))[:2];t=x,y
    m=[[v in t for v in r]for r in g]
    n=[0]*10
    for _ in[0]*4:
        g,m=[*map(list,zip(*g[::-1]))],[*map(list,zip(*m[::-1]))]
        for R,G in zip(m,g):
            for a,b,d in zip(R,R[1:],G[1:]):
                if a and~b&1 and d not in t:n[d]+=1
    z=min(range(10),key=lambda k:(n[k]or 9e9,k))
    for _ in[0]*512:
        g,m=[*map(list,zip(*g[::-1]))],[*map(list,zip(*m[::-1]))]
        m=[[A or B and d==z for A,B,d in zip(r,r[1:]+[0],row)]for r,row in zip(m,g)]
    b=[(i+j)&1^(v==y)for i,r in enumerate(g)for j,v in enumerate(r)if m[i][j]and v in t][0]
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==z and m[i][j]:g[i][j]=t[(i+j)&1^b]
    return g
