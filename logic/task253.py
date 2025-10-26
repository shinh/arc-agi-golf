def p(j):# collect corner colors
 a,b,c,d=map(max,zip(*((x*(x==y==u),x*(x==u==v),x*(x==y==v),v*(v==y==u))for r,s in zip(j,j[1:])for x,y,u,v in zip(r,r[1:],s,s[1:]))));return(a,a,c,c),(a,0,0,c),(b,0,0,d),(b,b,d,d)
