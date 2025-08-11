# Note task242 and task351 are very similar but best scores are quite different.
# Task242 53 bytes from theirs: 107 vs 54
# Task351 37 bytes from theirs: 107 vs 70
# Task400 37 bytes from theirs: 107 vs 70
def p(g):
    o=[]
    for r,rr in zip(g,g[::-1]):
        r=[rc for c,rc in zip(r,rr[::-1])if c<1]
        if r:o+=r,
    return o
