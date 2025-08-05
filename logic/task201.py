def p(g):
 D={};[D.setdefault(v,[]).append((i,j))for i,r in enumerate(g)for j,v in enumerate(r)]
 for k,v in D.items():
  if len(v)==4 and len({x for x,_ in v})==len({y for _,y in v})==2:o=k;t=v;break
 r,s=zip(*t);a=min(r);b=max(r);c=min(s);d=max(s)
 s=[row[c:d+1]for row in g[a:b+1]];h=[row[:]for row in g]
 for i in range(a,b+1):h[i][c:d+1]=[0]*(d-c+1)
 T=lambda m:[*map(list,zip(*m))];m=any(len({*r})<2 for r in s)
 if m:s=T(s);h=T(h)
 z=[(v,i,j)for i,r in enumerate(h)for j,v in enumerate(r)if v]
 if z:x=min(i for v,i,j in z);y=min(j for v,i,j in z);z=[(v,i-x,j-y)for v,i,j in z]
 P=set(sum(s,[]))-{0,o}
 if len(P)>1:
  p=min(P);q=max(P);L=lambda m,t:min(r.index(t)for r in m if t in r)
  if (L(s,q)>L(s,p))!=(L(h,q)>L(h,p)):w=max(j for _,_,j in z);z=[(v,i,w-j)for v,i,j in z]
 for v,i,j in z:i+=1;j+=1;0<=i<len(s)and 0<=j<len(s[0])and s[i].__setitem__(j,v)
 return T(s)if m else s
