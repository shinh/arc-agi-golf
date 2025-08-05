def p(g):
 h=len(g);w=len(g[0])
 bg=max(g[0]);v=set();b=[]
 d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
 for y in range(h):
  for x in range(w):
   if g[y][x]!=bg and (y,x)not in v:
    q=[(y,x)];v.add((y,x));c=[]
    for i,j in q:
     c.append((i,j))
     for di,dj in d:
      ni,nj=i+di,j+dj
      if 0<=ni<h and 0<=nj<w and g[ni][nj]==g[y][x] and (ni,nj)not in v:
       v.add((ni,nj));q.append((ni,nj))
    if len(c)>len(b):b=c
 sh=max(i for i,_ in b)-min(i for i,_ in b)+1
 sw=max(j for _,j in b)-min(j for _,j in b)+1
 for dy in(-1,0,1):
  for dx in(-1,0,1):
   if dy|dx:
    sy,sx=(sh+1)*dy,(sw+1)*dx;c=bg
    for y,x in b:
      ny, nx=y+sy, x+sx
      if 0<=ny<h and 0<=nx<w and g[ny][nx]!=bg:
       c=g[ny][nx];break
    k=1
    while c!=bg:
     f=False
     for y,x in b:
      ny, nx=y+sy*k, x+sx*k
      if 0<=ny<h and 0<=nx<w:g[ny][nx]=c;f=True
     if not f:break
     k+=1
 return g
