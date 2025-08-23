def p(g):#move 5s toward 2 cluster
 t=sum(g,[]);w=len(g[0]);y,x=divmod(t.index(2)+~w,w);o=[[2*(v==2)for v in r]for r in g]
 for i,v in enumerate(t):
  if v>4:o[max(y,min(y+3,i//w))][max(x,min(x+3,i%w))]=5
 return o
