def p(g):
    h=len(g);w=len(g[0]);r=[row[:]for row in g];i=0
    while i<h:
        if 8 in g[i]:
            s=i;L=[]
            while i<h and 8 in g[i]:
                L.append(max(j for j,v in enumerate(g[i])if v==8));i+=1
            e=i-1;n=e-s+1;M=max(L)
            if n==1:
                for c in range(M+1,w):r[s][c]=1
            elif L[-1]>L[0]:
                t=e+1
                if t<h:
                    for c in range(M+1,w):r[t][c]=1
            elif L[-1]<L[0]:
                for c in range(M+1,w):r[e-((c-M-1)%n)][c]=1
            elif min(L)<M:
                for c in range(M+1,w):r[s][c]=r[e][c]=1
            elif e+1<h:
                for c in range(M+1,w):r[e+1][c]=1
        else:i+=1
    return r
