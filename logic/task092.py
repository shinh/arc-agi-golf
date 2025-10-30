# hv flood fill
import re;s=re.sub
f=lambda g:[*zip(*eval(s(r'([1-9])(?:, \d)+, \1',lambda m:s(r'\d',m[1],m[0]),str(g))))]
p=lambda g:f(f(g))
