p=lambda g:[[[0,5,6,4,3,1,2,7,9,8][x]for x in g[0]]]*3
# p=lambda g:[[b"a\05\06\04\03\01\02\07\11\10"[x]for x in g[0]]]*3
# 46 (optimal is 43), minifier currently mangles this but should work as is
# p=lambda g:[[b"a	"[x]for x in g[0]]]*3
