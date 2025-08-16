# expand 5 block based on surrounding colors
def p(g):
    t=l=14;b=r=0
    for i in range(14):
        for j in range(14):
            if g[i][j]==5:t=min(t,i);b=max(b,i);l=min(l,j);r=max(r,j)
    o=create(14,14)
    for i in range(t,b+1):
        left=sum(v%5>0 for v in g[i][:l]);right=sum(v%5>0 for v in g[i][r+1:])
        o[i][l-left:r+1+right]=[5]*(r-l+1+left+right)
    for j in range(l,r+1):
        above=sum(r[j]%5>0 for r in g[:t]);below=sum(r[j]%5>0 for r in g[b+1:])
        for k in range(above):o[t-1-k][j]=5
        for k in range(below):o[b+1+k][j]=5
    return o
