import re
p=lambda g:[[int(re.search(r"([1-9]), \1, \1,.*\1, ((?!\1|0)\d), \1",str(g))[2])]]
