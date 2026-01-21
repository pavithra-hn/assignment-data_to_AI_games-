#  Tensor Operations

import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(a + b)
print(torch.dot(a, b))

# output
# tensor([5, 7, 9])
# tensor(32)