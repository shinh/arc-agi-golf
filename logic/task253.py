# rotate grid to reuse L pattern detection

def p(j):
 A=len(j)-1;c=[[0]*4for _ in[0]*4]
 for _ in[0]*4:
  for E in range(A):
   for k in range(A):
    if(W:=j[E][k])and j[E+1][k]==W and j[E][k+1]==W:c[0][0]=c[1][0]=c[0][1]=W
  j=[*zip(*j[::-1])];c=[*map(list,zip(*c[::-1]))]
 return c
