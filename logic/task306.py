def p(g):
 for a,b in zip(g,g[10:]):s=max(a,b);a[:]=b[:]=((max(s[:9],s[10:19],s[20:29])+[4])*(len(s)//9))[:-1]
 return g