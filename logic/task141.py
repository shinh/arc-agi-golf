def p(g):# draw diagonals from cell
 e=enumerate
 y,x,c=[(y,x,v)for y,r in e(g)for x,v in e(r)if v][0]
 return[[c*(Y in (X+y-x,y+x-X))for X,_ in e(g)]for Y,_ in e(g)]

