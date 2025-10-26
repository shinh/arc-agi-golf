def p(g):
 s=sum(g,[]);a=max({*s}-{0},key=s.count);b=sum({*s})-a
 h=[*zip(*filter(any,zip(*filter(any,[[x*(x==a)for x in r]for r in g]))))]
 for _ in 0,1:
  k=3-len(h);z=(0,)*len(h[0]);h=[z]*k*(0 in h[0])+h+[z]*k*(1-(0 in h[0]));h=[*zip(*h)]
 return[[x or b for x in r]for r in h]