def p(g):
    o=g
    for i in range(120):
        o=[*map(list,zip(*o[-2+(2 in o[-1])::-1]))]
    for c in set(sum(g,[]))-{0,2}:
        for i in range(120):
            g=[*map(list,zip(*g[-2+(c in g[-1])::-1]))]
        n=len(o)//len(g)
        y=0
        for r in g:
            for t in range(n):
                y+=1
                o[y][1:-1]=[c for c in r for t in range(n)]
        return o
