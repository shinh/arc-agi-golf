def p(g):
    # find biggest frame and recolor matching shapes
    for y in range(20):
        for x in range(20):
            if g[y][x]==5:
                n=0
                for ey in range(y+1,21):
                    if ey>19or g[ey][x]!=5:break
                    n+=1
                for ex in range(x+1,20):
                    if g[ey-1][ex]!=5:break
                    n+=1
                if n==12:
                    sx=x
                    sy=y

    for y in range(16):
        for x in range(16):
            if all((g[sy+dy+1][sx+dx+1]>0)==(g[y+dy][x+dx]>0)for dy in range(5)for dx in range(5)):
                for dy in range(5):
                    for dx in range(5):
                        g[y+dy][x+dx]=g[sy+dy+1][sx+dx+1]
    return g
