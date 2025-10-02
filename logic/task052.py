# p=lambda g:[[(r==r[:1]*3)*5]*3for r in g]# uniform row -> 5 else 0
# p=lambda g:[[(len({*r})<2)*5]*3for r in g]# uniform row -> 5 else 0
# p=lambda g:[[1//len({*r})*5]*3for r in g]# uniform row -> 5 else 0
# idea
# p=lambda g:[[len({*r})*3%7]*3for r in g]# uniform row -> 5 else 0


# p=lambda g:[[(a==b==c)*5]*3for a,b,c in g]# uniform row -> 5 else 0
# p=lambda g:[[(a,a==b)*5]*3for a,*b in g]# uniform row -> 5 else 0

# there's always a max of 2 different colors so this works since len never 3
p=lambda g:[[len({*r})%2*5]*3for r in g]# uniform row -> 5 else 0
