def p(g):
 #diagonals
 d=g[-2];a=d.index(max(d))
 for r in g[-3:~a-2:-1]:a-=1;r[a]=r[~a]=g[-1][len(d)//2]
 return g

