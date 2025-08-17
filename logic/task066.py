# connect 3 to 2 around blocks
def p(g):
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x]==2:
                ry=y
                rx=x
    for y in range(len(g)):
        for x in range(len(g[0])):
            dy=dx=0
            if g[y][x]==3 and g[y-1][x]==3:
                dy=1
            elif g[y][x]==3 and g[y][x-1]==3:
                dx=1
            else:
                continue

            cands=[]
            for dy,dx in ([dy,dx],[-dy,-dx]):
                ny=y
                nx=x
                o=[r*1for r in g]

                q=0
                t=0
                while t<100:
                    t+=1
                    o[ny][nx]=3
                    ny+=dy
                    nx+=dx
                    if not(0<=ny<len(g)and 0<=nx<len(g[0])):break
                    if g[ny][nx]==2:
                        cands.append((q,o))
                        break
                    if g[ny][nx]==8:
                        q+=1
                        ny-=dy
                        nx-=dx
                        if dy:
                            dy=0
                            dx=[-1,1][rx>nx]
                        else:
                            dy=[-1,1][ry>ny]
                            dx=0
                        ny+=dy
                        nx+=dx
                        if g[ny][nx]==8:break
            return min(cands,key=lambda t:t[0])[1]
