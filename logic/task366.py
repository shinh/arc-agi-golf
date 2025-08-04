def p(g):
 h,w=len(g),len(g[0])
 r=sum(len(set(R))==1 for R in g)
 c=sum(len({g[i][j]for i in range(h)})==1 for j in range(w))
 if r>c:k=h//2;o=h%2;a=g[:k];b=g[k+o:]
 else:k=w//2;o=w%2;a=[R[:k]for R in g];b=[R[k+o:]for R in g]
 if len({v for R in a for v in R})<=len({v for R in b for v in R}):B=[R[:]for R in a];O=b
 else:B=[R[:]for R in b];O=a
 f=lambda x:(lambda s:max(s,key=s.count))(sum(x,[]))
 bc=f(B);bg=f(O)
 H,W=len(O),len(O[0]);S=set();objs=[]
 for i in range(H):
  for j in range(W):
   if O[i][j]!=bg and(i,j)not in S:
    q=[(i,j)];S.add((i,j));o=[]
    while q:
     x,y=q.pop();o.append((O[x][y],(x,y)))
     for u,v in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=u<H and 0<=v<W and O[u][v]!=bg and(u,v)not in S:S.add((u,v));q.append((u,v))
    objs.append(o)
 if not objs:return B
 s=[v for o in objs for v,_ in o];oc=max(s,key=s.count)
 H,W=len(B),len(B[0]);pad=[[bc]*(W+2)for _ in range(H+2)]
 for i,R in enumerate(B):pad[i+1][1:-1]=R
 for o in objs:
  cs=[p for _,p in o];mi=min(i for i,j in cs);mj=min(j for i,j in cs);ma=max(i for i,j in cs);mb=max(j for i,j in cs)
  pat=[(bc,(i,j))if v==oc else(v,(i,j))for v,(i,j) in o]
  for i in range(mi-1,ma+2):pat+=[(bc,(i,mj-1)),(bc,(i,mb+1))]
  for j in range(mj-1,mb+2):pat+=[(bc,(mi-1,j)),(bc,(ma+1,j))]
  pi=min(i for _,(i,j) in pat);pj=min(j for _,(i,j) in pat)
  pat=[(v,(i-pi,j-pj))for v,(i,j) in pat]
  ph=max(i for _,(i,j) in pat)+1;pw=max(j for _,(i,j) in pat)+1
  occ=set()
  for si in range(len(pad)-ph+1):
   for sj in range(len(pad[0])-pw+1):
    if all(pad[si+a][sj+b]==v for v,(a,b) in pat):occ.add((si-1,sj-1))
  if occ:
   di,dj=next(iter(occ));di-=pi;dj-=pj
   for v,(i,j) in o:
    ii=i+di;jj=j+dj
    if 0<=ii<H and 0<=jj<W:B[ii][jj]=v
 return B

