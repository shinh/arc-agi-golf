def p(m):f=sum(m,[]);g,n=f.count,len(m);l=g(f[i:=f.index(min(f,key=g))])+4>>2;return[x[i%n:][:l]for x in m[i//n:][:l]]
