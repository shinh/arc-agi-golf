# repeat the tile wherever its map is colored
def p(g,R=range(9)):a,b=next((y-y%3,x-x%3)for y in R for x in R if g[y][x]);return[[g[a+y//3][b+x//3]&g[a+y%3][b+x%3]for x in R]for y in R]
