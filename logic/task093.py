# expand 5 block based on surrounding colors
def p(g):
    # find bounding box and extend edges by neighbor counts
    f=sum(g,[]);a=f.index(5);d=195-f[::-1].index(5);t,l=divmod(a,14);b,r=divmod(d,14);o=create(14,14)
    for y in range(t,b+1):
        a=sum(v%5>0 for v in g[y][:l]);d=sum(v%5>0 for v in g[y][r+1:])
        o[y][l-a:r+d+1]=[5]*(r-l+1+a+d)
    for x in range(l,r+1):
        for i in range(sum(r[x]%5>0 for r in g[:t])):o[t-1-i][x]=5
        for i in range(sum(r[x]%5>0 for r in g[b+1:])):o[b+1+i][x]=5
    return o
