def p(g):# draw diagonals from cell
 b=sum(g,[]);y,x=divmod(b.index(c:=max(b)),n:=len(g));r=range(n)# flatten grid, find colored cell
 return[[c*(Y in (X+y-x,y+x-X))for X in r]for Y in r]# fill diagonals with color

