def p(g):#fill 8s between 5s
 for _ in[0]*4:
  for r,n in zip(g,g[1:]):
   if 0<(c:=r.count(5))<3:
    a=r.index(5);e=(9-r[::-1].index(5),10)[c<2>n.index(5)^a<1];r[a+1:e]=[8]*~(a-e)
  g=[*map(list,zip(*g[::-1]))]
 return g
