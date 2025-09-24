def p(g):# draw diagonals
 r=range(len(g));c,y,x=max((g[y][x],y,x)for y in r for x in r)# find cell
 return[[c*(abs(Y-y)==abs(X-x))for X in r]for Y in r]# fill diagonals

