p=lambda g:max(([r[i%7:][:3]for r in g[i//7:][:3]]for i in range(49)),key=lambda B:sum((v==1)*9+v//8for v in sum(B,[])))#3x31>8
