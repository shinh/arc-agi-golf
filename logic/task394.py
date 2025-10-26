def p(g):
 n=len(g);e=3-(n<7);y,x=divmod(sum(g,[]).index(0),n);b=g[y].count(0);return[g[y+a+e-(y+a>=n-e)*2*e][x:x+b]for a in range(b)]