def p(g):#two4x4s
 a=g[0][1]<3;c=g[1][0]<3;c+=(a^c)*4
 # repeat rows of a 4x4 block at two positions
 return[[3*(e<=x<e+4)for x in range(9)]for e in[9]*a+4*[c]+4*[c^4]+[9]*(a^1)]
