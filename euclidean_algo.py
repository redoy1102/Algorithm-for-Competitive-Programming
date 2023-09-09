def euclidean_algo(a, b):
  if b == 0:
    return a
  else:
    return euclidean_algo(b, a % b)


a, b = 5, 10
print(euclidean_algo(a, b))