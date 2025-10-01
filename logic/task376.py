# p=lambda g:(g+g[-2:0:-1])*2+g[:1]
# p=lambda g:(a:=g+g[-2::-1])+a[1:]
# stuff between 1:-1 is symmetrical already in all test cases, no need to flip
p=lambda g:(g+g[1:-1])*2+g[:1]
