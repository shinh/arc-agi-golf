# repeat pattern of first column
p=lambda g:(c:=next(zip(*g)))and(c*3,c[::-1]*3)
