# expand each center row into solid 3x3 blocks
def p(g):
 for i in range(1,len(g),4):
  g[i-1:i+2]=[sum(([c+5]*3+[5]for c in g[i][1::4]),[])[:-1]]*3
 return g

