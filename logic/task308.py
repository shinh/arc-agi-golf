def p(g):
 t=sum(g,[]);b=max(t,key=t.count);d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v-b:
    a,m,c,n=d.get(v,(i,i,j,j));d[v]=min(a,i),max(m,i),min(c,j),max(n,j)
 s=max(max(m-a,n-c)for a,m,c,n in d.values())+1;o=[[b]*s for _ in[0]*s]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v-b:
    a,m,c,n=d[v];o[i-a+(s-m+a>>1)][j-c+(s-n+c>>1)]=v
 return o