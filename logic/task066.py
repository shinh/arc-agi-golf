# connect 3 to 2 around blocks
def p(g):
    h=len(g);w=len(g[0]);tr=0
    s=[(i,j)for i in range(h)for j in range(w)if g[i][j]==3]
    t=[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]
    if t[0][0]!=t[1][0]:
        g=[list(r)for r in zip(*g)];h,w=w,h;tr=1
        s=[(x,y)for y,x in s];t=[(x,y)for y,x in t]
    o=[v for r in g for v in r if v*(v-2)*(v-3)][0]
    y3=s[0][0];x3l=min(x for y,x in s);x3r=max(x for y,x in s)
    y2=t[0][0];x2l=min(x for y,x in t);x2r=max(x for y,x in t)
    for j in sorted(range(w),key=lambda j:abs(j-x3r)):
        if g[y3][j]==0 and o in g[y3][j-1:j+2:2]:
            e=x3r if j>x3r else x3l
            if all(g[y3][k]==0 for k in range(min(j,e)+1,max(j,e))):
                if g[y2][j]==0 and o in [r[j]for r in g[y2-1:y2+2:2]]:
                    e=x2r if j>x2r else x2l
                    if all(g[y2][k]==0 for k in range(min(j,e)+1,max(j,e))):
                        if all(g[y][j]==0 for y in range(min(y3,y2)+1,max(y3,y2))):
                            c=j;break
    d=1 if c>=x3r else -1
    for x in range(x3r+d,c+d,d):g[y3][x]=3
    d=1 if c>=x2r else -1
    for x in range(x2r+d,c+d,d):g[y2][x]=3
    for y in range(min(y3,y2),max(y3,y2)+1):g[y][c]=3
    for y,x in t:g[y][x]=2
    if tr:g=[list(r)for r in zip(*g)]
    return g

