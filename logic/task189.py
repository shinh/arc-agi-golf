def p(g):#put corner pattern on 3s
 A=g[2][0]>7;B=g[0][2]>7;R=range(6)
 return[[[v:=g[3*A+y][3*B+x],g[7-7*A+y//3][7-7*B+x//3]][v==3]for x in R]for y in R]
