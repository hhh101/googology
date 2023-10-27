x=[0,1,2,3,4,5,6,7,8,9]
def d(n,a):
  f=n
  i=0
  for i in range(len(n)):
    f[i]+=a
    i+=1
  return f
def expand(n,m):
  k=n
  if n[-1]==0:
    k.pop()
    return k
  else:
    l=n[-1]
    bp=[]
    k.pop()
    p=k[-1]
    bp.append(p)
    while p>l-1:
      bp.append(l-2)
      k.pop()
      p=k[-1]
    delta=(l-1)-p
    i=1
    for i in range(m+1):
      k.extend(d(bp,delta))
      i+=1
    return k
b=1
while x!=[]:
  x=expand(x,b)
  b+=1
print(b)
