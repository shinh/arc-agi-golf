# repeat the tile wherever its map is colored
def p(g,R=range(9)):a=(i:=(s:=sum(g,[])).index(max(s)))//27*3;b=i%9//3*3;return[[g[a+y//3][b+x//3]&g[a+y%3][b+x%3]for x in R]for y in R]
