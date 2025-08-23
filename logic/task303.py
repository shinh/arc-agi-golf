def p(g):
 # 0 rows/cols ->2
 return[[2 if sum(r)<1 or{*z}<={0,2}else v for v,z in zip(r,zip(*g))]for r in g]
