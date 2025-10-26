def p(j):
 a=b=c=d=0
 for r,s in zip(j,j[1:]):
  for x,y,u,v in zip(r,r[1:],s,s[1:]):
   a|=x*(x==y==u);b|=x*(x==u==v);c|=x*(x==y==v);d|=v*(v==y==u)
 return (a,a,c,c),(a,0,0,c),(b,0,0,d),(b,b,d,d)