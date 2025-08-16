def p(g):#put corner pattern on 3s
 E=enumerate;A=g[2]==[8]*9;B=all(r[2]==8 for r in g);a=7-7*A;b=7-7*B;c=3*A;d=3*B
 return[[[v,g[a+y//3][b+x//3]][v==3]for x,v in E(r)]for y,r in E([r[d:d+6]for r in g[c:c+6]])]
