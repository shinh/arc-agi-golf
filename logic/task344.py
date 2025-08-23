# swap 2 next to 3 with 0 and 8
def p(g):
 for _ in 0,0:g=zip(*[map(int,str(r)[1::3].replace('23','08').replace('32','80'))for r in g])
 return[*g]
