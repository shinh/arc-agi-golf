def p(g):
 for o in range(10):
  t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==o]
  if len(t)==4 and len({i for i,_ in t})==len({j for _,j in t})==2:break
 r,s=zip(*t);a=min(r);b=max(r);c=min(s);d=max(s)
 s=[r[c:d+1]for r in g[a:b+1]]
 z=[(v,i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v and not(a<=i<=b and c<=j<=d)]
 if any(len({*r})<2 for r in s):s=[*map(list,zip(*s))];z=[(v,j,i)for v,i,j in z];m=1
 else:m=0
 if z:x=min(i for v,i,j in z);y=min(j for v,i,j in z);z=[(v,i-x,j-y)for v,i,j in z]
 P=sorted(set(sum(s,[]))-{0,o})
 if P[1:]:
  p,q=P[0],P[-1];L=lambda m,t:min(r.index(t)for r in m if t in r)
  G=lambda t:min(j for v,i,j in z if v==t)
  if (L(s,q)>L(s,p))!=(G(q)>G(p)):w=max(j for _,_,j in z);z=[(v,i,w-j)for v,i,j in z]
 for v,i,j in z:i+=1;j+=1;len(s)>i and len(s[0])>j and s[i].__setitem__(j,v)
 return [*map(list,zip(*s))] if m else s
