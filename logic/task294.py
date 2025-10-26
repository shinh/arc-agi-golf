import re
p=lambda g:eval(re.sub("(?<=5.{31})(?<=5..)5(?=..5)(?=.{31}5)",'2',str(g)))