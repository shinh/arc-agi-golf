def p(g):
 # move 3x3 block marked by 4 to its 4x offset
 y,x=divmod(sum(g,[]).index(4),11);Y=y&3;X=x&3
 o=[[5*(v==5)for v in r]for r in g]
 for k in 0,1,2:o[Y*4+k][X*4:X*4+3]=g[y-Y+k][x-X:x-X+3]
 return o

