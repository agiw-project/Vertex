import hashlib
from pearhash import PearsonHasher

#It creates a different hash function for each distinct n
def generate_hash_function(n):
  def myhash(x):
    x = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    for i in range(n):
      x = hashlib.sha256(str(x).encode('utf-8')).hexdigest()

    b = bytes(x[:8], encoding='utf-8')
    output = int.from_bytes(b, byteorder='big', signed=False)
    return output

  return myhash

def generate_hash_function2(n):
  def myhash(x):
    output = hash(x)
    for i in range(n):
      output = hash(output)
    return output

  return myhash


def generate_hash_function_pearson_hash(n):
  def myhash(x):
    # Set desired hash length in bytes
    hasher = PearsonHasher(1)
    x = "".join(x)
    b = hasher.hash(bytes(x, encoding='utf-8'))
    for i in range(n):
      b = hasher.hash(b)
    output = int.from_bytes(b, byteorder='big', signed=False)
    return output

  return myhash