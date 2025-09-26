# if in a black inside corner that doesn't extend make yellow
# if black and yellow neighbor make yellow
# rotate 4x to only check rule in 1 direction
def p(g,R=range(20)):
    for _ in R:
        for y in R:
            for x in R:
                try:
                    if g[y][x]==0 and g[y+1][x]==4 or g[y][x]==g[y+2][x+1]==g[y+1][x+2]==0 and g[y+1][x]==g[y][x+1]==5:
                        g[y][x]=4
                except:0
        g = [*map(list,zip(*g[::-1]))]
    return g