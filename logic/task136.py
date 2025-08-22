def p(g):# diagonals from first 1 & last 2
 r=sum(g,[])
 y,x,Y,X=divmod(r.index(1),10)+divmod(99-r[::-1].index(2),10)
 while ~x*~y:g[y][x]=1;x-=1;y-=1
 while X<9>Y:X+=1;Y+=1;g[Y][X]=2
 return g
