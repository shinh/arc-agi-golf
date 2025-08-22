# 660
# longest runs -> cross arms
def p(g):
 bg=max(g[0],key=g[0].count);m=[];L=0
 for c in range(10):
  mx=0,
  for r in g+[*zip(*g)]:
   if c in r:
    a=r.index(c);b=len(r)-r[::-1].index(c);l=r[a:b];k=len(l)
    n1=next((i for i in range(k)if l[i]-c),k);n2=next((i for i in range(k)if l[~i]-c),k)
    q=max(n1,n2);n=q*2+k-n1-n2
    mx=max(mx,(n,q))
  mx[0]and c-bg and(m.append([c,*mx])or(L:=max(L,mx[0])))
 o=[[bg]*L for _ in[0]*L]
 for c,n,q in m:
  n+=n==2;y=(L-n)//2
  for _ in[0]*4:
   for i in range(q):o[y][y+i]=o[y+i][y]=c
   o=[*map(list,zip(*o[::-1]))]
 return o
