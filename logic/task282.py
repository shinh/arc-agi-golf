import re
p=lambda g,t=9:t and p(eval(re.sub(r"(.{7})(.{22})0, 5, 0(.{22})\1",r"5,1,5\2 1,0,1\3 5,1,5",str(g))),t-1)or g