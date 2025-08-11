# Note task242 and task351 are very similar but best scores are quite different.
# Task242 53 bytes from theirs: 107 vs 54
# Task351 37 bytes from theirs: 107 vs 70
# Task400 37 bytes from theirs: 107 vs 70
def p(g,R=range(24)):
    o=[]
    for y in R:
        r=[g[23-y][23-x]for x in R if g[y][x]==1]
        if r:o+=r,
    return o
