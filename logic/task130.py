def p(g):# 3x3 mode
 return[[max(b:=sum((r[x:x+3]for r in g[y:y+3]),[]),key=b.count)for x in(0,3,6)]for y in(0,3,6)]
