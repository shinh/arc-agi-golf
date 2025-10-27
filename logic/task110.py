# It seemed solvable with `p=lambda g:[eval(f'[{re.findall(re.sub("0","[^0]",str(r)[1:-1]), str(g))[0]}]') for r in g]`, but failed in 1 case.
p=lambda g:[[*map(max,*filter(lambda s:max(a*b*(a^b)for a,b in zip(r,s))<1,g))]for r in g]
