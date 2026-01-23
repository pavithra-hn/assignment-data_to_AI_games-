# Dataset & DataLoader

from torch.utils.data import DataLoader, TensorDataset
import torch

x = torch.randn(100, 2)
y = torch.sum(x, dim=1)

dataset = TensorDataset(x, y)
loader = DataLoader(dataset, batch_size=10)

for batch_x, batch_y in loader:
    print(batch_x.shape)
    break

# output : 
# torch.Size([10, 2])