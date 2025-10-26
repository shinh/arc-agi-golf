import re
# It seemed solvable with `p=lambda g:[eval(f'[{re.findall(re.sub("0","[^0]",str(r)[1:-1]), str(g))[0]}]') for r in g]`, but failed in 1 case.
p=lambda g:[[max(l) for l in zip(*[eval(f'[{m}]') for m in re.findall(re.sub("(\d)",r"[0\1]", re.sub("0",".",str(r)[1:-1])), str(g))])] for r in g]