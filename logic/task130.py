t=0,3,6;p=lambda g:[[max(b:=sum((r[x:x+3]for r in g[y:y+3]),[]),key=b.count)for x in t]for y in t]#3x3 mode
