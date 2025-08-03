def p(g):
 a=len(g)//2;b=g[a].index(1);o=[r[:] for r in g]
 if b==4:
  r=1
  try:r+=g[a+3].index(1)<b
  except:0
  if r>1:
   o[a][:b]=[2]*b;o[a-1][1:g[a-1].index(1)-1]=[2]*(g[a-1].index(1)-2)
   for y in(a-2,a+1,a+2):o[y][1]=2
  else:
   for y,w in((a-1,g[a-1].index(1)-2),(a,b-1),(a+1,g[a+1].index(1)-4)):
    o[y][1:w+1]=[2]*w
 else:
  r=(b-1)//2
  for d in range(-r,r+1):
   y=a+d;L=g[y].index(1)
   if d==0:o[y][1:b]=[2]*(b-1)
   elif L<5:o[y][1]=2
   else:
    try:n=g[y].index(1,L+1)
    except:n=10
    p=2 if n-L>2 else 3;o[y][1]=o[y][p]=2
 return o
