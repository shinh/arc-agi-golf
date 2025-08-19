# 328
def p(g):
    ok=lambda sy,sx:all(g[sy+y][sx+x]==0 or(-1<y<3 and -1<x<3)for y in range(-1,4)for x in range(-1,4)if 0<=sy+y<len(g)and 0<=sx+x<len(g[0]))

    for sy in range(len(g)-2):
        for sx in range(len(g[0])-2):
            s=[g[sy+y][sx+x]for y in range(3)for x in range(3)]
            if ok(sy,sx)and len({*s})>2:
                for dy in range(len(g)-2):
                    for dx in range(len(g[0])-2):
                        d=[g[dy+y][dx+x]for y in range(3)for x in range(3)]
                        n=sdc=0
                        for sc,dc in zip(s,d):
                            if dc:
                                n+=1
                                sdc=dc
                        if ok(dy,dx)and n and all(dc==0 or dc==sc for sc,dc in zip(s,d))and s.count(sdc)==n:
                            for y in range(3):
                                for x in range(3):
                                    g[dy+y][dx+x]=g[sy+y][sx+x]
    return g
