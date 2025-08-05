def p(g):
 h=len(g);w=len(g[0])
 F={(i,j)for i,r in enumerate(g) if len(set(r))==1 for j in range(w)}|{(i,j)for j in range(w) if len({g[i][j]for i in range(h)})==1 for i in range(h)}
 c=g[next(iter(F))[0]][next(iter(F))[1]]
 G=[[g[i][j] if (i,j)not in F else-1 for j in range(w)]for i in range(h)]
 V=[[0]*w for _ in g];O=[]
 for i in range(h):
  for j in range(w):
   if G[i][j]<0 or V[i][j]:continue
   q=[(i,j)];V[i][j]=1;o=[]
   while q:
    y,x=q.pop();o+=[(G[y][x],y,x)]
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     ny=y+dy;nx=x+dx
     if 0<=ny<h and 0<=nx<w and G[ny][nx]>=0 and not V[ny][nx]:V[ny][nx]=1;q+=[(ny,nx)]
   O+=[o]
 b=0
 o=[o for o in O if any(v==4 for v,_,_ in o)][0]
 mi=min(i for _,i,_ in o);mj=min(j for _,_,j in o)
 o=[(v,i-mi,j-mj)for v,i,j in o if v!=5]
 H=max(i for _,i,_ in o)+1;W=max(j for _,_,j in o)+1
 P=[(i,j)for v,i,j in o if v==4]
 cy=(min(i for i,_ in P)+max(i for i,_ in P))//2
 cx=(min(j for _,j in P)+max(j for _,j in P))//2
 dy=(H+1)*cy;dx=(W+1)*cx
 out=[[b]*w for _ in g]
 for i,j in F:out[i][j]=c
 for v,i,j in o:
  y=i+dy;x=j+dx
  if 0<=y<h and 0<=x<w:out[y][x]=v
 return out
