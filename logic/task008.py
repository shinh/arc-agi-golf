import re
# extend 2s toward 8s via rotation
p=lambda g,n=39:-n*g or p([*zip(*[[[8*(c>7)or(p==2)*2,c][not re.search("2, 0[,0 ]+8",s:=str(g))or"2, 8"in s]for c,p in zip(r,[0,*r])]for r in g][::-1])],n-1)
