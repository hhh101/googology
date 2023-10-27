x=[0,1,2,3,4,5,6,7,8,9]
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
    while p!=l-1:
      bp.append(p)
      k.pop()
      p=k[-1]
    bp.reverse()
    k.extend(bp*m)
    return k
b=1
while x!=[]:
  x=expand(x,b)
  b+=1
print(b)
