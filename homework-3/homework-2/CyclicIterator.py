import time
class CyclicIterator:

  def __init__(self, value):
      self.value = value
      self.iter = iter(self.value)


  def __iter__(self):
    return self

  def __next__(self):
    try:
        return(next(self.iter))
    except StopIteration:
        self.iter = iter(self.value)
        return next(self.iter)


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
    time.sleep(1)
