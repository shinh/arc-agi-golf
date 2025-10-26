def p(g):
 A=[i for i,r in enumerate(g)if 4 in r];t=A[0];v=A[-1]
 B=[i for i,c in enumerate(zip(*g))if 4 in c];s=B[0];u=B[-1]
 o=[r[s:u+1]for r in g[t:v+1]]
 for r in g[t:v+1]:r[s:u+1]=[0]*(u-s+1)
 h=[*zip(*filter(any,zip(*filter(any,g))))]
 m=any(a[0]==b[0]for a,b in zip(h,o[1:]))
 for i,r in enumerate(h):o[i+1][1:-1]=(r,r[::-1])[not m]
 return o