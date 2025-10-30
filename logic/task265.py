import re
p=lambda g,k=3:-k*g or p(eval(re.sub(r'[02], [02](.{52})[02], 0(?!.{52}2, 5, 0)','2,2\g<1>2,2',str(g[::-1]))),k-1)#.
