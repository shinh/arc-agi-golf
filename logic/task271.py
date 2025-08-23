R=range(7)
# pick 3x3 with most 1s then 8s
p=lambda g:max((sum((v==1)*9+v//8for r in B for v in r),B)for B in([r[x:x+3]for r in g[y:y+3]]for y in R for x in R))[1]
