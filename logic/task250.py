def p(g):#move 5s toward 2 cluster
 t=sum(g,[]);w=len(g[0]);y,x=divmod(t.index(2),w);y0,y1,x0,x1=y-1,y+2,x-1,x+2;o=[[2*(v==2)for v in r]for r in g]
 for i,v in enumerate(t):
  if v>4:Y,X=divmod(i,w);o[min(y1,max(y0,Y))][min(x1,max(x0,X))]=5
 return o
