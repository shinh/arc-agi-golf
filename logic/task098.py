# erosion via flood fill using rot90 trick
p=lambda g,o=0,n=4,z=zip:n and p([[a*(b>0)for a,b in z(r,r[1:]+(0,))]for r in z(*g[::-1])],o or g,n-1,z)or[[a*(b<1)for a,b in z(*t)]for t in z(o,g)]
