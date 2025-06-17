left,right=0,10
eps=1e-12
f=lambda x:x**3-5*(x**2)+10*x-80
while right-left>eps:
    mid=(left+right)/2
    if f(mid)>0:
        right=mid
    else:
        left=mid
print(f'{mid:.9f}')