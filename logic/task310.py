def p(m):f=sum(m,[]);g=f.count;i=f.index(min(f,key=g));n=len(m);l=g(f[i])+4>>2;return[x[i%n:][:l]for x in m[i//n:][:l]]
