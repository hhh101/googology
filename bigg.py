def f(n,x,m):
  d=0
  e=0
  k=len(n)-1
  while n[k]>=n[-1]:
    k-=1
  if x[-1]>0:
    while n[k]>=n[-1] or x[k]>=x[-1]:
      k-=1
    d=n[-1]-n[k]
    e=x[-1]-n[k]-1
  n.pop()
  x.pop()
  if k>0:
    i=m
    while i>0:
      n.append(n[k]+d)
      x.append(x[k]+e)
      k+=1
      i-=1
  return n, x
b=3
x=[-1,0,1]
y=[-1,0,999]
while x!=[]:
  p=f(x,y,b)
  x=p[0]
  y=p[1]
  b+=1
print(b)
