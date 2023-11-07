x=1
y=2
z=3
ra=112233
p = 0
while p < (x+y+z)**2:
    p = p+1
    print(p)
if p%2==0:
    print(f"{ra} - {x}")
else:
    print(f"{ra} + ’-’ + 'y'")