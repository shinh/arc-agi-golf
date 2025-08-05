def p(g):
 h,w=len(g),len(g[0])
 r=sum(len({*R})<2 for R in g)
 c=sum(len({*C})<2 for C in zip(*g))
 if r>c:a=g[:h//2];b=g[(h+1)//2:]
 else:a=[R[:w//2]for R in g];b=[R[(w+1)//2:]for R in g]
 if len({*sum(a,[])})>len({*sum(b,[])}) :a,b=b,a
 B=[R[:]for R in a];O=b
 d=max(F:=sum(B,[]),key=F.count)
 e=max(G:=sum(O,[]),key=G.count);G=[v for v in G if v-e]
 if not G:return B
 f=max(G,key=G.count)
 H,W=len(B),len(B[0]);P=[[d]*(W+2)for _ in range(H+2)]
 for i,R in enumerate(B):P[i+1][1:-1]=R
 h,w=len(O),len(O[0]);s=set()
 for i in range(h):
  for j in range(w):
   if O[i][j]-e and(i,j)not in s:
    q=[(i,j)];s.add((i,j));o=[]
    while q:
     x,y=q.pop();o.append((O[x][y],(x,y)))
     for u,v in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=u<h and 0<=v<w and O[u][v]-e and(u,v)not in s:s.add((u,v));q.append((u,v))
    X,Y=zip(*(p for _,p in o));mi,ma=min(X),max(X);mj,mb=min(Y),max(Y)
    p=[[(v,(i,j)),(d,(i,j))][v==f]for v,(i,j) in o]
    for x in range(mi-1,ma+2):p+=[(d,(x,mj-1)),(d,(x,mb+1))]
    for y in range(mj-1,mb+2):p+=[(d,(mi-1,y)),(d,(ma+1,y))]
    pi=min(i for _,(i,j) in p);pj=min(j for _,(i,j) in p)
    p=[(v,(i-pi,j-pj))for v,(i,j) in p]
    ph=max(i for _,(i,j) in p)+1;pw=max(j for _,(i,j) in p)+1
    t=set()
    for si in range(len(P)-ph+1):
     for sj in range(len(P[0])-pw+1):
      if all(P[si+a][sj+b]==v for v,(a,b) in p):t.add((si-1,sj-1))
    if t:
     di,dj=next(iter(t));di-=pi;dj-=pj
     for v,(x,y) in o:
      x+=di;y+=dj
      if 0<=x<H and 0<=y<W:B[x][y]=v
 return B
