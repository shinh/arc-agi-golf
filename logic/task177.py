# crop bbox & mirror
# crop bbox & mirror
f=filter
p=lambda g:[*zip(*f(any,[*zip(*f(any,g))][::-1]))]
