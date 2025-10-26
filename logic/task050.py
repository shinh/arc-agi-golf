import re
h=lambda x:eval(re.sub('8(, 0)+, 8',lambda m:m[0].replace('0','3'),str(x)))
p=lambda g:[*zip(*h([*zip(*h(g))]))]