# Multiclass Classification

import torch
import torch.nn as nn

X = torch.randn(10, 4)
y = torch.tensor([0,1,2,0,1,2,0,1,2,1])

model = nn.Linear(4, 3)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(100):
    output = model(X)
    loss = loss_fn(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(torch.argmax(model(X), dim=1))

# output : 
# tensor([0, 1, 2, 0, 1, 2, 0, 1, 2, 1])

