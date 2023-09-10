# O(sqrt())
def euclidean_algo(a, b):
  if b == 0:
    return a
  return euclidean_algo(b, a%b)

print(euclidean_algo(100, 5))
