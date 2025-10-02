# map 5's column to color and repeat
# p=lambda g:[[-r.index(5)%3+2]*3for r in g]
# p=lambda g:g and[-g[0].index(5)%3+2]*3+p(g[1:])
# p=lambda g:[[b%3+c%4+2]*3for a,b,c in g]
p=lambda g:[[~a%4+b%4]*3for a,b,c in g]

# 2 red
# 3 green
# 4 yellow

# 0 -> 2 red
# 1 -> 4 yellow
# 2 -> 3 green

# -r.index(5)%3+2
# hash((*r,))%5
# a*2+b-c&7,b,c
# (a*2+b)%7+2,b,c
# b%3+c%4+2,b,c


# for i in range(9999):
#     for j in range(5,9):
#         if hash((5,0,0,i))%j == 2 and hash((0,5,0,i))%j == 4 and hash((0,0,5,i))%j == 3:
#             print([i,j])
# 1/0