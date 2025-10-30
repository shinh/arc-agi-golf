def p(g):
 y=bytes(map(any,g));Y=y.find(1);Y1=y.rfind(1)
 z=bytes(map(any,zip(*g)));X=z.find(1);X1=z.rfind(1)
 a=g[Y+2][X+2]
 return [[(v,(a,g[Y][X])[Y<=i<=Y1 and X<=j<=X1])[a in(r[X+1],r[X1-1],g[Y+1][j],g[Y1-1][j])]for j,v in enumerate(r)]for i,r in enumerate(g)]