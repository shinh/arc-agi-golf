def p(j):
 A=range;t=0,4,8
 for r in t:
  for s in t:
   # expand 3x3 block & add lines
   if sum(j[r+W][s+l]<1for W in A(3)for l in A(3))>4:
    return[[5*(3in(i%4,c%4))or j[r+i//4][s+c//4]for c in A(11)]for i in A(11)]
