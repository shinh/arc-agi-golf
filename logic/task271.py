_=range(7);p=lambda g:max([[r[x:x+3]for r in g[y:y+3]]for y in _ for x in _],key=lambda B:sum((v==1)*9+v//8for v in sum(B,[])))#3x31>8
