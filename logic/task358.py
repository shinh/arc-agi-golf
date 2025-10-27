# rotate
p=lambda g,n=4:n and p([(b:=[*filter(abs,a)])[2:]and(b*9)[-a.index(b[0])%len(b):][:len(a)]or a for a in zip(*g[::-1])],n-1)or g
