def p(j):
 b=range(11)
 # expand 3x3 block & add lines
 return next([[5*(3in(i%4,c%4))or j[r+i//4][s+c//4]for c in b]for i in b]for r in(0,4,8)for s in(0,4,8)if sum(j[r+w//3][s+w%3]<1for w in range(9))>4)
