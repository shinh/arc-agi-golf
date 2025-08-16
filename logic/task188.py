# left if halves equal else top half
def p(g):w=len(g[0])//2;return(l:=[r[:w]for r in g])*(l==[r[-w:]for r in g])or g[:len(g)//2]
