def p(g):#two4x4s
 a=g[0][1]<3;b=g[1][0]<3;c=4*(a^b)+b;r=[0]*9
 # repeat rows of a 4x4 block at two positions
 return [r]*a+[r[:e]+[3]*4+r[e+4:]for e in(c,c^4)for _ in[0]*4]+[r]*(a<1)
