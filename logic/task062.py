def p(g):
 #mirror arm
 d=sum(r.count(2)for r in g)*2
 for _ in[0]*4:
  g=[*zip(*g[::-1])]
  for r in range(10):
   if sum(w:=g[r])==d==w.count(2)*2:
    for t in g[r+1:r+r+2]:
     if sum(t)>t.count(2)*2:g[r]=t
     r-=1
 return[[c or 3for c in r]for r in g]
