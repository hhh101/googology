x=[0,999999999999]
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
    while p>l-1:
      bp.append(p)
      k.pop()
      p=k[-1]
    delta=(l-1)-p
    bp.insert(0,l-delta)
    i=1
    bp.reverse()
    bp.insert(0,l-delta-1)
    for i in range(m+1):
      k.extend(d(bp,delta))
      i+=1
    return k
b=1
while x!=[]:
  x=expand(x,b)
  b+=1
print(b)
