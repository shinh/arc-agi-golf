def p(g):
    # move each 3x3 block without 0 to matching hole ignoring color 2
    R=range;z=zip;f=filter;r=R(3);O=()
    for x in R(len(g[0])-2):
        for y in R(len(g)-2):
            o=[g[y+i][x:x+3]for i in r]
            if min(s:={*sum(o,[])})*(len(s)-1):
                O+=o,
                for i in r:g[y+i][x:x+3]=0,0,0
    g=[*map(list,z(*f(any,z(*f(any,g)))))]
    for o in O:
        for _ in R(4):
            for y in R(len(g)-2):
                for x in R(len(g[0])-2):
                    if all((o[i][j]!=2)==(g[y+i][x+j]>0)for i in r for j in r):
                        for i in r:g[y+i][x:x+3]=o[i]
                        break
                else:continue
                break
            else:o=[*z(*o[::-1])];continue
            break
    return g

