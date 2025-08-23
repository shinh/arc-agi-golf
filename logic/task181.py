def p(j):# mirror central band
 A=6*(j[3][3]<1)
 for r in j[:3]:r[A:A+3]=r[5:2:-1]
 return j