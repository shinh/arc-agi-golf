def p(g):# uniq q
 s=sum(g,[]);m=len(g);n=m>>1;d=s.index(min(s,key=s.count))
 return[[r[n+1:],r[:n]][d%m<n]for r in[g[n+1:],g[:n]][d<m*n]]
