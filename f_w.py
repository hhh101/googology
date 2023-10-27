def A(n,m):
  if n==0:
    return m+1
  else:
    if m==0:
      return A(n-1,1)
    else:
      return A(m-1,A(n-1,m))
print(A(A(A(9**9**9,0),0),0))
