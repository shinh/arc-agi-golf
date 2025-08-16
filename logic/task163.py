def p(g):
 # move 3x3 block marked by 4 to its 4x offset
 i=sum(g,[]).index(4);y=i//11;x=i%11
 a=y&-4;b=x&-4;y%=4;x%=4
 o=[[5*(v==5)for v in r]for r in g]
 for k in 0,1,2:o[y*4+k][x*4:x*4+3]=g[a+k][b:b+3]
 return o

