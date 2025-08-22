# expand diagonals around 2x2 block
def p(g):
 r,c=min((y,x)for y in range(6)for x in range(6)if g[y][x])
 a,b=g[r][c:c+2];e,d=g[r+1][c:c+2]
 L=min(2,c);R=min(2,4-c)
 for t in g[r-min(2,r):r]:t[c-L:c]=[d]*L;t[c+2:c+2+R]=[e]*R
 for t in g[r+2:r+2+min(2,4-r)]:t[c-L:c]=[b]*L;t[c+2:c+2+R]=[a]*R
 return g
