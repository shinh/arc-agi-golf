import re
p=lambda g:[[int(re.search(r"([1-9]), \1, \1,.*\1, ((?!\1)[1-9]), \1",str(g))[2])]]
