def p(g):
    h=len(g);w=len(g[0]);g=[r[:]for r in g];i=0
    while i<h:
        r=g[i]
        if i+1<h:
            s=g[i+1];c1=[j for j,v in enumerate(r)if v==8];c2=[j for j,v in enumerate(s)if v==8]
            if c1 or c2:
                m=max(c1+c2);p=c1[0]%2 if c1 else (c2[0]+1)%2
                if all(r[j]==(8 if j%2==p else 0) and s[j]==(8 if j%2!=p else 0) for j in range(m+1)) and all(r[j]==s[j]==0 for j in range(m+1,w)):
                    for j in range(m+1,w): (r if j%2==p else s)[j]=1
                    i+=2;continue
        c=[j for j,v in enumerate(r)if v==8]
        if c:
            if len(c)==1 and i+1<h and 8 not in g[i+1]:
                g[i+1][c[0]+1:]=[1]*(w-c[0]-1)
            elif len(c)>1 and not(i+1<h and c[-1]+1<w and g[i+1][c[-1]+1]==8):
                r[c[-1]+1:]=[1]*(w-c[-1]-1)
        i+=1
    return g
