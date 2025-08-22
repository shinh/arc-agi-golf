# crop bounding box and mirror horizontally
p=lambda g:[*zip(*filter(any,[*zip(*filter(any,g))][::-1]))]
