def p(g):
 b=max(t:=sum(g,[]),key=t.count);d={};s=1;E=enumerate
 for i,r in E(g):
  for j,v in E(r):
   if v-b:a,m,c,n=d.get(v,(i,i,j,j));a=min(a,i);m=max(m,i);c=min(c,j);n=max(n,j);d[v]=a,m,c,n;s=max(s,m-a+1,n-c+1)
 o=[[b]*s for _ in[0]*s]
 for i,r in E(g):
  for j,v in E(r):
   if v-b:a,m,c,n=d[v];o[i-a+(s-m+a>>1)][j-c+(s-n+c>>1)]=v
 return o