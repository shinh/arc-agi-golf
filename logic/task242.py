def p(g):
 z=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v<1]
 a,b=min(i for i,_ in z),max(i for i,_ in z)+1;c,d=min(j for _,j in z),max(j for _,j in z)+1
 f=lambda m:sum(m[i][j]<1 for i in range(a,b)for j in range(c,d))
 m=[r[::-1]for r in g];h=g[::-1];m=m if f(m)<=f(h)else h
 return [r[c:d]for r in m[a:b]]
