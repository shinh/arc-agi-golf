# 660
# longest runs -> cross arms
def p(g):
 R=range;bg=max(g[0],key=g[0].count);t=g+[*zip(*g)];m=[];L=0
 for c in R(10):
  mx=0,
  for r in t:
   if c in r:a=r.index(c);b=len(r)-r[::-1].index(c);k=b-a;n1=next((i for i in R(k)if r[a+i]-c),k);n2=next((i for i in R(k)if r[b-1-i]-c),k);mx=max(mx,(k+abs(n1-n2),max(n1,n2)))
  if mx[0]and c-bg:L=max(L,mx[0]);m+=[(c,*mx)]
 o=[[bg]*L for _ in R(L)]
 for c,n,q in m:
  n+=n==2;y=L-n>>1
  for _ in R(4):
   for i in R(q):o[y][y+i]=o[y+i][y]=c
   o=[*map(list,zip(*o[::-1]))]
 return o
