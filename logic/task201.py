def p(g):
 t,*_,v=[i for i,r in enumerate(g)if 4in r];G=g[t:v+1];s,*_,u=[i for i,c in enumerate(zip(*G))if 4in c]
 o=[r[s:u+1]for r in G]
 for r in G:r[s:u+1]=[0]*(u-s+1)
 Z=[*zip(zip(*filter(sum,zip(*filter(sum,g)))),o[1:])]
 m=any(a[0]==b[0]for a,b in Z)
 for a,b in Z:b[1:-1]=a[::m or-1]
 return o
