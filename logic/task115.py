def p(g):
 # dedup first row or column
 f=dict.fromkeys;return[[*zip(f(next(zip(*g))))],[[*f(g[0])]]][len({*g[0]})>1]
