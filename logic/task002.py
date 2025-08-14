# rotate the image 90 degrees 4x times with zip(*g[::-1]) instead of applying logic at 4 different directions

# def p(g):
#     for _ in range(80):
#         g=[[max(a,b==1)for a,b in zip(r,[*r[1:],1])]for r in zip(*g[::-1])]
#     return [[[4,0,9,3][c]for c in r]for r in g]

# iterate using recursion instead of an outer for loop, convert to expected output colors when n==1 so that n==0 can just return g

# p=lambda g,n=64:n and p([[[max(a,b==1),[4,0,9,3][a]][n<2]for a,b in zip(r,[*r[1:],1])]for r in zip(*g[::-1])],n-1)or g

# use a magic function instead of looking up from [4,0,*,3]

# p=lambda g,n=64:n and p([[[max(a,b==1),~-a%5+a//2][n<2]for a,b in zip(r,[*r[1:],1])]for r in zip(*g[::-1])],n-1)or g

# improve magic function and also use `a` only once inside magic function which may be useful for further improvements
# 0 1 3
# 4 0 3

# p=lambda g,n=64:n and p([[[max(a,b==1),4*-~-a%11][n<2]for a,b in zip(r,[*r[1:],1])]for r in zip(*g[::-1])],n-1)or g

# possible improvements:
#   better magic formulas for max(a,b==1) and also 4*-~-a%11
#   rather than rotate with zip and [::-1], take coordinates [-x][y] and loop in range(len(g))
#       if doing that, you could have a single loop and use mod and div to get x and y
#           this could be combined with looping for n too (would need to be a def instead of lambda
#           maybe instead of using len(g) you could hardcode some factorial so that it goes through the list an integer number of times (factorial of largest size would work) - this could then be put into a default assignment of a parameter).

# The AI found a better magic formula:
#p=lambda g,n=64:n and p([[[a or b==1,4*-~-a%11][n<2]for a,b in zip(r,r[1:]+(1,))]for r in zip(*g[::-1])],n-1)or g

# Better recursion
p=lambda g,n=63:-n*g or p([[[a or b==1,4*-~-a%11][n<1]for a,b in zip(r,r[1:]+(1,))]for r in zip(*g[::-1])],n-1)
