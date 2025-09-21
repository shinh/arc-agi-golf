# 0/9 mask
p=lambda g:[[~(a|b)&8for a,b in zip(r,r[4:])]for r in g]
