def p(g):
    # move each 3x3 block without 0 to matching hole ignoring color 2
    r=range(3);O=[]
    for x in range(len(g[0])-2):
        for y in range(len(g)-2):
            o=[g[y+i][x:x+3]for i in r];s={*sum(o,[])}
            if len(s)>1 and 0 not in s:
                O+=o,
                for i in r:g[y+i][x:x+3]=0,0,0
    g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
    for o in O:
        for _ in 0,1,2,3:
            for y in range(len(g)-2):
                for x in range(len(g[0])-2):
                    if all((v!=2)==(g[y+i][x+j]>0)for i in r for j,v in enumerate(o[i])):
                        for i in r:g[y+i][x:x+3]=o[i]
                        break
                else:continue
                break
            else:o=[*zip(*o[::-1])];continue
            break
    return g

