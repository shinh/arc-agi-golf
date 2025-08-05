def p(g):
 h=len(g);w=len(g[0]);H=h*3;W=w*3
 B=[[0]*W for _ in[0]*H]
 for y in range(h):
  for x in range(w):B[h+y][w+x]=g[y][x]
 P=(-1,0,1);V=set();O=[]
 for y in range(H):
  for x in range(W):
   if B[y][x]and(y,x)not in V:
    q=[(y,x)];V.add((y,x));S=set();C={}
    for Y,X in q:
     S.add((Y,X));v=B[Y][X];C[v]=C.get(v,0)+1
     for a in P:
      for b in P:
       if a|b:
        y2=Y+a;x2=X+b
        if 0<=y2<H and 0<=x2<W and B[y2][x2]and(y2,x2)not in V:V.add((y2,x2));q+=[(y2,x2)]
    O+=[(S,C)]
 t=max(O,key=lambda o:len(o[1]));O.remove(t)
 d={}
 for _,c in O:
  for k,v in c.items():d[k]=d.get(k,0)+v
 m=max(d,key=d.get);S,_=t
 mi=min(y for y,_ in S);mj=min(x for _,x in S)
 T=[(y-mi,x-mj,B[y][x])for y,x in S]
 A=[(y,x)for y,x,v in T if v==m];Z=[(y,x)for y,x,v in T if v!=m]
 th=max(y for y,_,_ in T)+1;tw=max(x for _,x,_ in T)+1;C=[]
 for k in range(1,6):
  for y in range(H-th*k+1):
   for x in range(W-tw*k+1):
    S={(y+i*k+dy,x+j*k+dx)for i,j in A for dy in range(k)for dx in range(k)}
    if {B[Y][X]for Y,X in S}=={m}and not any(B[y+i*k+dy][x+j*k+dx]for i,j in Z for dy in range(k)for dx in range(k)):
     U=set()
     for s,_ in O:
      if s&S:U|=s
     if len(U)==len(S):C+=[(y,x,k)]
 for y,x,k in C:
  for i,j,v in T:
   for dy in range(k):
    for dx in range(k):B[y+i*k+dy][x+j*k+dx]=v
 return[r[w:2*w]for r in B[h:2*h]]
