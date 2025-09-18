def p(g):#two4x4s
 a,b=g[0][1]<3,g[1][0]<3;c=4*(a^b)+b
 # repeat rows of a 4x4 block at two positions
 return[[3*(e<=x<e+4)for x in range(9)]for e in[9]*a+[c]*4+[c^4]*4+[9]*(1-a)]
