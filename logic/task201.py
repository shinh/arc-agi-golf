# crop the frame of 4s and move the other shape inside
def p(g):
    sx=sy=sx2=sy2=99;ex=ey=ex2=ey2=-1
    for y in range(13):
        for x in range(13):
            if g[y][x]==4:
                if x<sx:sx=x
                if y<sy:sy=y
                if ex<x:ex=x
                if ey<y:ey=y
    o=[r[sx:ex+1]for r in g[sy:ey+1]]
    for y in range(13):
        for x in range(13):
            if g[y][x]and(x<sx or y<sy or ex<x or ey<y):
                if x<sx2:sx2=x
                if y<sy2:sy2=y
                if ex2<x:ex2=x
                if ey2<y:ey2=y
    no_mirror=any(g[sy2+y][sx2]==o[y+1][0]for y in range(ey2-sy2+1))
    for y in range(ey2-sy2+1):
        for x in range(ex2-sx2+1):
            o[y+1][[-x-2,x+1][no_mirror]]=g[y+sy2][x+sx2]
    return o
