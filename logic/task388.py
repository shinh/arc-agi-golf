def p(g):
 for j in range(len(g[0])):
  if any(r[j]for r in g):
   for r in g:
    if not r[j]:r[j]=8
 return [r+r for r in g]*2
