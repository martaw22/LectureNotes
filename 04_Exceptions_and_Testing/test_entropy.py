'''Tests for entropy.'''

import entropy

def test_one_shot(x):
  value = entropy.entropy([x])
  assert(value == 0)

def test_distribution():
  try:
    value = entropy.entropy([1.0, 1.0])
  except ValueError:
    pass
  
