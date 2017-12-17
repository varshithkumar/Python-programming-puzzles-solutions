def array_left_rotation(a, n, k):
  if len(a) == 1:
    return a
  k %= n
  a = a[k:] + a[:k]   
  return a 