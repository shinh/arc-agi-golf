# mids->3x3
p=lambda g:[(sum(([c+5]*3+[5]for c in g[i&-4|1][1::4]),[])[:-1],r)[i==3]for i,r in enumerate(g)]

