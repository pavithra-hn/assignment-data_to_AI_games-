# Save & Load Model


import torch

model = torch.nn.Linear(1, 1)
torch.save(model.state_dict(), "model.pth")

model2 = torch.nn.Linear(1, 1)
model2.load_state_dict(torch.load("model.pth"))

print("Model loaded")

# output :
# Model loaded