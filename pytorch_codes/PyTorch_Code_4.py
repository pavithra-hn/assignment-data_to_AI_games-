# Neural Network (Supervised)

import torch

model = torch.nn.Sequential(
    torch.nn.Linear(2, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 1)
)

x = torch.randn(20, 2)
y = torch.sum(x, dim=1, keepdim=True)

loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

for _ in range(500):
    pred = model(x)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(model(torch.tensor([[2.0, 3.0]])))

# output : 
# tensor([[4.7674]], grad_fn=<AddmmBackward0>)

