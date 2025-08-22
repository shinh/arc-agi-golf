# repeat first 6 columns 9 times and crop
p=lambda g:[(r[:6]*9)[:len(r)*2]for r in g]
