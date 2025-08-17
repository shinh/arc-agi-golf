# rotate grid to reuse L pattern detection

def p(j):
 c=[[0]*4for _ in[0]*4]
 for _ in[0]*4:
  for r,s in zip(j,j[1:]):
   for a,b,d in zip(r,r[1:],s):
    if a==b==d>0:c[0][0]=c[1][0]=c[0][1]=a
  j=[*zip(*j[::-1])];c=[*map(list,zip(*c[::-1]))]
 return c
