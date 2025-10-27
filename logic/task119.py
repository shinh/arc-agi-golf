import re
p=lambda g,t=7:-t*g or p(eval(re.sub("0(?=.{34}(.{35})*(8.{34}8|3.{34}2))","3",str([*zip(*g[::-1])]))),t-1)