# linear Regression (Supervised)

import torch

# Data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Model
model = torch.nn.Linear(1, 1)

# Loss & Optimizer
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training
for epoch in range(100):
    y_pred = model(X)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Prediction for 5:", model(torch.tensor([[5.0]])).item())



# output :
# Prediction for 5: 9.496824264526367

#  Learns y = 2x
# Supervised learning using labeled data
