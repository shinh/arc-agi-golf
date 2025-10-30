import re
p=lambda g,k=39:-k*g or p(eval(re.sub('5, '*(t:=k//4%10),('142'[('4'in str(g))+('1'in str(g))]+', ')*t,str([*zip(*g[::-1])]))),k-1)