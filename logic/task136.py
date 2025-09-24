def p(g):# diagonals from first 1 & last 2
 r=sum(g,[])
 for v,s,t in((1,-1,r.index(1)),(2,1,99-r[::-1].index(2))):
  y,x=divmod(t,10)
  while-1<x<10>y>-1:g[y][x]=v;x+=s;y+=s
 return g
