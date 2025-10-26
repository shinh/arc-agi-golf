def p(g):
 r=range;O=()
 for x in r(len(g[0])-2):
  for y in r(len(g)-2):
   o=[g[y+i][x:x+3]for i in r(3)];s={*sum(o,[])}
   if 0not in s and len(s)>1:
    O+=o,
    for i in r(3):g[y+i][x:x+3]=0,0,0
 g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 for o in O:
  for _ in r(4):
   for y in r(len(g)-2):
    for x in r(len(g[0])-2):
     if all((o[i][j]!=2)==(g[y+i][x+j]>0)for i in r(3)for j in r(3)):
      for i in r(3):g[y+i][x:x+3]=o[i]
      break
    else:continue
    break
   else:o=[*zip(*o[::-1])];continue
   break
 return g