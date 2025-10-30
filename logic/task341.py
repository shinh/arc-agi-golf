def p(l,E=enumerate):# row/col 8 bridge
 for _ in 0,1:
  for i in [i for i,r in E(l)if len({*r})>2][1:-1]:
   r=l[i]=[*l[i]];a,*_,b=(j for j,v in E(r)if v)
   while b>a:b-=1;r[b]=r[b]or 8
  l=[*zip(*l)]
 return l
