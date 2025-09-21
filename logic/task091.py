def p(g):y,x=zip(*(divmod(i,len(g[0]))for i,v in enumerate(sum(g,[]))if v==5));return[r[min(x):max(x)+1]for r in g[y[0]-(y[0]>0):y[-1]+2]]
