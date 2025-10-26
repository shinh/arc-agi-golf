import re
p=lambda g,t=1:-t*g or p(eval(re.sub(r'1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1',r'0,2,0\1 2,2,2\2 0,2,0',str(g))),t-1)