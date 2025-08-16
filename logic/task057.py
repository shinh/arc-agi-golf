# crop nonzero rows/cols then double
p=lambda g,f=filter:[[*r,*r]for r in zip(*f(any,zip(*f(any,g))))]

