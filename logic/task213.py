def p(g):
    # orient then palette
    c=next(v for r in g for v in r if v%5);o=sum(c in r for r in g)>sum(c in r for r in zip(*g));d=[*dict.fromkeys(v for r in(zip(*g)if o else g)for v in r if v%5)];l=len(d)
    return (d,)*l if o else[[v]*l for v in d]
