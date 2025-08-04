def p(g):
  c={}
  for r in g:
    for v in r:c[v]=c.get(v,0)+1
  bg=max(c,key=c.get)
  d={}
  for i,r in enumerate(g):
    for j,v in enumerate(r):
      if v!=bg:d.setdefault(v,[]).append((i,j))
  I=[];s=0
  for k,P in d.items():
    mi=min(i for i,j in P);ma=max(i for i,j in P)
    mj=min(j for i,j in P);mb=max(j for i,j in P)
    M=max(ma-mi+1,mb-mj+1)
    S=set(P);mx=0
    while S:
      st=[S.pop()];a=B=st[0][1]
      while st:
        i,j=st.pop()
        for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
          t=(i+di,j+dj)
          if t in S:
            S.remove(t);st.append(t)
            u=t[1]
            if u<a:a=u
            if u>B:B=u
      w=B-a+1
      if w>mx:mx=w
    sc=M+mx
    if len(P)==1:s=1
    def mv(c):
      a=min(j for i,j in c);A=max(j for i,j in c);d=a+A
      return [(i,d-j) for i,j in c]
    def mh(c):
      a=min(i for i,j in c);A=max(i for i,j in c);d=a+A
      return [(d-i,j) for i,j in c]
    def md(c):
      a=min(i for i,j in c);b=min(j for i,j in c)
      return [(j-b+a,i-a+b) for i,j in c]
    def mc(c):return mv(md(mv(c)))
    def ul(c):return min(i for i,j in c),min(j for i,j in c)
    def f(c):
      a,b=ul(c);S=set(c)
      return((a+1,b)in S)+((a,b+1)in S)
    V=[P,mv(P),mc(P),mh(P)]
    B=max(V,key=f)
    a,b=ul(B)
    I.append((sc,k,[(i-a,j-b) for i,j in B]))
  I.sort(key=lambda x:(-x[0],-x[1]))
  n=len(I);m=n if s else n+1
  z=2*m-1
  pts=[];mx=0
  for i,(_,k,C) in enumerate(I):
    for x,y in C:
      x+=i;y+=i
      pts.append((x,y,k))
      if x>mx:mx=x
      if y>mx:mx=y
  if mx>=z:z=mx+1
  R=[[bg]*z for _ in range(z)]
  for i,j,k in pts:R[i][j]=k
  for _ in range(3):
    R=[list(r) for r in zip(*R[::-1])]
    for i,j,k in pts:R[i][j]=k
  return R
