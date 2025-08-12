# erosion via flood fill using rot90 trick
p=lambda g,o=None,n=4:n and p([[a*(b>0)for a,b in zip(r,r[1:]+(0,))]for r in zip(*g[::-1])],o or g,n-1)or[[a*(b==0)for a,b in zip(orow,row)]for orow,row in zip(o,g)]
