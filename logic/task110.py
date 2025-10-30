# It seemed solvable with `p=lambda g:[eval(f'[{re.findall(re.sub("0","[^0]",str(r)[1:-1]), str(g))[0]}]') for r in g]`, but failed in 1 case.
p=lambda g:[[*map(max,*[s for s in g if all(a*b<1for a,b in zip(r,s)if a-b)])]for r in g]
