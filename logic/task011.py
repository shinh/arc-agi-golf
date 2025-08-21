def p(j):
 B=range(11);t=0,4,8
 for r in t:
  for s in t:
   # expand 3x3 block & add lines
   if sum(j[r+w//3][s+w%3]<1for w in range(9))>4:
    return[[5*(3in(i%4,c%4))or j[r+i//4][s+c//4]for c in B]for i in B]
