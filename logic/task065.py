def p(g):# uniq q
 s=sum(g,[]);m=len(g);n=m>>1;d=s.index(min(s,key=s.count))
 return[r[-n*(d%m>=n):][:n]for r in g[-n*(d>=m*n):][:n]]
