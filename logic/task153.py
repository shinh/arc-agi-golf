def p(g):
 # crop+pad+fill
 s=sum(g,[]);b,a=sorted({*s}-{0},key=s.count)
 h=[r for r in zip(*(c for c in zip(*g)if a in c))if a in r]
 for _ in 0,1:
  k=3-len(h);z=(0,)*len(h[0]);h=[z]*k+h if 0 in h[0]else h+[z]*k;h=[*zip(*h)]
 return[[x or b for x in r]for r in h]
