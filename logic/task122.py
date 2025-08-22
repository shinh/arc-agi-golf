# Far from the best (100)
# slide the 3x3 chunk below/right of a 2,3 stripe
def p(g):
 for sx in range(2):
  for y in range(len(g)-2):
   for x in range(len(g[0])-2):
    if[[r[x+1]for r in g[y:y+4]],g[y+1][x:x+4]][sx]==[2,3]*2:
     for dy in 2,1,0:
      for dx in 2,1,0:
       if dy!=1 or dx!=1:
        g[y+dy+2-sx*2][x+dx+sx*2]=g[y+dy][x+dx]
        g[y+dy][x+dx]=0
     return g
