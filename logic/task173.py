# 328
def p(g):
    # replicate the colorful 3x3 block onto any matching empty window
    ok=lambda sy,sx:all(g[sy+y][sx+x]==0 or(-1<y<3 and -1<x<3)for y in range(-1,4)for x in range(-1,4)if 0<=sy+y<len(g)and 0<=sx+x<len(g[0]))
    for sy in range(len(g)-2):
        for sx in range(len(g[0])-2):
            s=[g[sy+y][sx+x]for y in range(3)for x in range(3)]
            if ok(sy,sx)and len({*s})>2:
                for dy in range(len(g)-2):
                    for dx in range(len(g[0])-2):
                        if ok(dy,dx)and(z:=[(sc,dc)for sc,dc in zip(s,(g[dy+y][dx+x]for y in range(3)for x in range(3)))if dc])and all(sc==dc for sc,dc in z)and s.count(z[0][0])==len(z):
                            for y in range(3):
                                g[dy+y][dx:dx+3]=g[sy+y][sx:sx+3]
    return g
