def p(g):
    h=len(g);w=len(g[0])
    t=h;b=0;l=w;r=0
    for i in range(h):
        for j in range(w):
            if g[i][j]==5:
                t=min(t,i);b=max(b,i);l=min(l,j);r=max(r,j)
    o=create(h,w)
    for i in range(t,b+1):
        left=sum(g[i][k] and g[i][k]!=5 for k in range(l))
        right=sum(g[i][k] and g[i][k]!=5 for k in range(r+1,w))
        row=o[i]
        for j in range(l-left,r+1+right):
            if 0<=j<w:row[j]=5
    for j in range(l,r+1):
        above=sum(g[i][j] and g[i][j]!=5 for i in range(t))
        below=sum(g[i][j] and g[i][j]!=5 for i in range(b+1,h))
        for k in range(1,above+1):o[t-k][j]=5
        for k in range(1,below+1):o[b+k][j]=5
    return o
