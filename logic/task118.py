def p(g):
 # expand rare color into cross
 # fill small gaps, find longest line, extend to cross
 h=len(g);w=len(g[0])
 t=sum(g,[]);c=min(t,key=t.count)
 S={divmod(i,w)for i,v in enumerate(t)if v==c}
 p=0
 while p-len(S):
  p=len(S)
  for _ in 0,1:
   for y in range(h):
    q=-9
    for x in range(w):
     if(y,x)in S:
      if x-q<5:S|={(y,t)for t in range(q,x)}
      q=x
   h,w=w,h;S={(x,y)for y,x in S}
 L=0;M=set()
 for _ in 0,1:
  for y in range(h):
   x=0
   while x<w:
    if(y,x)in S:
     z=x
     while z<w and(y,z)in S:z+=1
     d=z-x
     if d>L:L=d;M=set()
     if d==L and all((y-1,t)not in S and(y+1,t)not in S for t in range(x,z)):M.add((y,x+d//2))
     x=z
    x+=1
  h,w=w,h;S={(x,y)for y,x in S};M={(x,y)for y,x in M}
 m=L//2
 M|={(y,x)for y,x in S if{(y-1,x),(y+1,x)}&S and{(y,x-1),(y,x+1)}&S}
 for y,x in M:
  for d in range(-m,m+1):
   0<=y+d<h and S.add((y+d,x))
   0<=x+d<w and S.add((y,x+d))
 for y,x in S:g[y][x]=(8,c)[g[y][x]==c]
 return g
