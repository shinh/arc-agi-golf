# cross for each 2x2 of 2s
p=lambda g:(k:=sum(all(t)for r,s in zip(g,g[1:])for t in zip(r,r[1:],s,s[1:])),((k>0,0,k>1),(0,k>2,0),(k>3,0,k>4)))[1]
