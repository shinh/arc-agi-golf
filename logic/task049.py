def p(g):
 # rare color bbox
 f=sum(g,[]);y,x=zip(*(divmod(i,len(g[0]))for i,a in enumerate(f)if a==min({*f}-{0},key=f.count)));return[r[min(x):max(x)+1]for r in g[min(y):max(y)+1]]
