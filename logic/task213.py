def p(g):
    # orient then palette
    c=next(v for r in g for v in r if v%5);v=sum(c in r for r in g)>sum(c in r for r in zip(*g));d=[]
    for r in zip(*g)if v else g:
        for c in r:
            if c%5 and c not in d:
                d+=c,
                if v:break
    return [d]*len(d)if v else[[c]*len(d)for c in d]
