def p(g):
 #mirror arm
 d=sum(r.count(2)for r in g)*2
 for _ in[0]*4:
  g=[*zip(*g)][::-1]
  for r in range(10):
   if sum(w:=g[r])==d==w.count(2)*2:
    for y in range(min(r,8-r)+1):
     if sum(t:=g[r+1+y])>t.count(2)*2:g[r-y]=t
 return[[c or 3for c in r]for r in g]
