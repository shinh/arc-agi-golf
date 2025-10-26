import re
p=lambda j:eval(re.sub('1, 0(?=, 1)','1,2',str(j)))