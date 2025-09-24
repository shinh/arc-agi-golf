def p(g):# expand patterns horizontally then vertically
 for _ in 0,1:
  r=next(r for r in g if(S:=[i for i,v in enumerate(r)if v])[1:])
  R=r[(a:=S[0]):S[-1]+1];r[:]=(R*32)[-a%len(R):][:len(r)];g=[*map(list,zip(*g))]
 return g
