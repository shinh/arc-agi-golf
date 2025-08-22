# mids->3x3
p=lambda g:[(sum(([c+5]*3+[5]for c in g[i-i%4+1][1::4]),[])[:-1],g[i])[i%4>2]for i in range(len(g))]

