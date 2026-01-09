#  AutoEncoder (Unsupervised)

import torch

model = torch.nn.Sequential(
    torch.nn.Linear(4, 2),
    torch.nn.ReLU(),
    torch.nn.Linear(2, 4)
)

x = torch.randn(50, 4)
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

for _ in range(500):
    pred = model(x)
    loss = loss_fn(pred, x)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Reconstruction done")
