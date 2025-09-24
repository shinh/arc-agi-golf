def p(g):# shift 4's 3x3 chunk by 4
 y,x=divmod(sum(g,[]).index(4),11);o=[[5*(v==5)for v in r]for r in g]
 for k in 0,1,2:o[y%4*4+k][x%4*4:x%4*4+3]=g[y-y%4+k][x&-4:][:3]
 return o
