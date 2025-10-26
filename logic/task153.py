def p(g):
 s=sum(g,[]);a=max({*s}-{0},key=s.count);b=sum({*s})-a
 h=[*zip(*[c for c in zip(*[r for r in g if a in r])if a in c])]
 for _ in 0,1:
  k=3-len(h);z=(0,)*len(h[0]);t=0 in h[0];h=[z]*k*t+h+[z]*k*(1-t);h=[*zip(*h)]
 return[[x or b for x in r]for r in h]
