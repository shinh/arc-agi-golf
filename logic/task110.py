def p(g):
    # brute-force tile size
    for q in range(1,30):
        for p in range(1,30):
            t=[[0]*p for _ in range(q)]
            for y,r in enumerate(g):
                for x,v in enumerate(r):
                    if v:
                        tv=t[y%q][x%p]
                        if tv and tv!=v:break
                        t[y%q][x%p]=v
                else:continue
                break
            else:return[[t[y%q][x%p]for x in range(29)]for y in range(29)]
