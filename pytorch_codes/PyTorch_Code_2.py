# Binary Classification


import torch
import torch.nn as nn

X = torch.tensor([[0.0],[1.0],[2.0],[3.0]])
y = torch.tensor([[0.0],[0.0],[1.0],[1.0]])

model = nn.Sequential(
    nn.Linear(1,1),
    nn.Sigmoid()
)

loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

for _ in range(200):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(model(torch.tensor([[1.5]])).item())

# output : 
# 00.5743870735168457

# here we used the binary classification to predict the output
