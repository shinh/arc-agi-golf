def p(g):
 # crop+pad+fill
 s=sum(g,[]);a=max(y:={*s}-{0},key=s.count);b=sum(y)-a
 h=[r for r in zip(*(c for c in zip(*g)if a in c))if a in r]
 for _ in 0,1:
  k=3-len(h);z=(0,)*len(h[0]);t=0 in h[0];h=[z]*k*t+h+[z]*k*(1-t);h=[*zip(*h)]
 return[[x or b for x in r]for r in h]
