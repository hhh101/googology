def f(n):
  return n**n
def g(n):
  if n==0:
    return 2:
  else:
    return f(g(n-1))
def h(n):
  if n==0:
    return 2:
  else:
    return g(h(n-1))
def i(n):
  if n==0:
    return 2:
  else:
    return h(i(n-1))
print(i(i(i(i(9**9**9)))))
