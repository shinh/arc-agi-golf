def p(g):
 h,w=len(g),len(g[0])
 r=sum(len({*R})<2 for R in g)
 c=sum(len({*C})<2 for C in zip(*g))
 if r>c:a=g[:h//2];b=g[(h+1)//2:]
 else:a=[R[:w//2]for R in g];b=[R[(w+1)//2:]for R in g]
 if len({*sum(a,[])})>len({*sum(b,[])}) :a,b=b,a
 B=[R[:]for R in a];O=b
 fb=sum(B,[]);bc=max(fb,key=fb.count)
 fo=sum(O,[]);bg=max(fo,key=fo.count);fo=[v for v in fo if v-bg]
 if not fo:return B
 oc=max(fo,key=fo.count)
 H,W=len(O),len(O[0]);S=set();objs=[]
 for i in range(H):
  for j in range(W):
   if O[i][j]-bg and(i,j)not in S:
    q=[(i,j)];S.add((i,j));o=[]
    while q:
     x,y=q.pop();o.append((O[x][y],(x,y)))
     for u,v in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=u<H and 0<=v<W and O[u][v]-bg and(u,v)not in S:S.add((u,v));q.append((u,v))
    objs.append(o)
 H,W=len(B),len(B[0]);pad=[[bc]*(W+2)for _ in range(H+2)]
 for i,R in enumerate(B):pad[i+1][1:-1]=R
 for o in objs:
  cs=[p for _,p in o];xs,ys=zip(*cs);mi=min(xs);mj=min(ys);ma=max(xs);mb=max(ys)
  pat=[[ (v,(i,j)),(bc,(i,j)) ][v==oc]for v,(i,j) in o]
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
