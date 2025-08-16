def p(g):
 a=max(r.count(8)for r in g);c=sum(g,[]).count;q=(c(5)-a-2)/2-c(8)/a
 return[[8*(q>0),8*(q>1),8*(q>2)],[0,0,8*(q>3)],[0,0,0]]#flat
