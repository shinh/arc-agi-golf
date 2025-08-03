def p(g):
 r=2 if g[2]==[8]*9 else 6;c=2 if [r[2] for r in g]==[8]*9 else 6
 R=[r[:c] if c>4 else r[c+1:] for r in (g[:r] if r>4 else g[r+1:])]
 A=[r[-2:] if c>4 else r[:2] for r in (g[-2:] if r>4 else g[:2])]
 return [[A[y//3][x//3] if v==3 else v for x,v in enumerate(r)]for y,r in enumerate(R)]
