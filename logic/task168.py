import re;p=lambda g,t=3:-t*g or p(eval(re.sub(r"0(?=(.{25}(.{29})*)[1-9].{31}[1-9].{2}[1-9])",str(max(max(g))),str([*zip(*g[::-1])]))),t-1)
