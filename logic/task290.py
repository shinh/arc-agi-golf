def p(g):
 l=t=99;r=B=0;s=set()
 for y,R in enumerate(g):
  for x,c in enumerate(R):
   if c:
    s|={c}
    if x<l:l=x
    if x>r:r=x
    if y<t:t=y
    if y>B:B=y
 a,b=s
 return[[c and [b,a][c!=a]for c in g[y][l:r+1]]for y in range(t,B+1)]

