def p(g):
 b=max(g[0],key=g[0].count)
 for _ in[0]*4:
  for r in g:
   for x in range(len(r)-2):
    if(c:=r[x])-b and(x<1or r[x-1]==b)and b in r[x+1:x+3]:
     for j in range(x,len(r)):
      if(u:=r[j])-b and u-c:
       if r[j+1]==u:r[x:j]=[c]*(j-x)
       break
  g=[*map(list,zip(*g[::-1]))]
 return g
