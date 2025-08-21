def p(g):
 # stripes
 (y1,x1,c1),(y2,x2,c2)=sorted((y,x,c)for y,r in enumerate(g)for x,c in enumerate(r)if c)
 b=x1*x2<1 or x1==x2 or y1*y2>0>=abs(x1-x2)-abs(y1-y2)
 if b<1:g=[*zip(*g)];(y1,c1),(y2,c2)=sorted(((x1,c1),(x2,c2)))
 w=len(g[0]);d=y2-y1;g[y1::2*d]=[[c1]*w]*len(g[y1::2*d]);g[y2::2*d]=[[c2]*w]*len(g[y2::2*d])
 return((*zip(*g),),g)[b]
