def p(g):
 # stripes
 (y1,x1,c1),(y2,x2,c2)=sorted((y,x,c)for y,r in enumerate(g)for x,c in enumerate(r)if c)
 d=y2-y1
 b=y1>0<d
 if b<1:g=[*zip(*g)];(y1,c1),(y2,c2)=sorted(((x1,c1),(x2,c2)));d=y2-y1
 w=len(g[0]);c=c1,c2
 for k,y in enumerate(range(y1,len(g),d)):g[y]=[c[k&1]]*w
 return((*zip(*g),),g)[b]
