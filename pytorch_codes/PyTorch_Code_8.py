# Loss Visualization

import torch
import matplotlib.pyplot as plt

losses = []
x = torch.tensor([[1.0], [2.0]])
y = torch.tensor([[2.0], [4.0]])

model = torch.nn.Linear(1, 1)
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(50):
    loss = loss_fn(model(x), y)
    losses.append(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

plt.plot(losses)
plt.show()

# output : 
# See PyTorch_Code_8_output.png for the loss plot
