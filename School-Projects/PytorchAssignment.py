# Install PyTorch and TorchVision
import torch
import torch.nn as nn
import torch.optim as optim

# Define a Neural Network model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(10, 9)
        self.fc2 = nn.Linear(9, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create an instance of the neural network
model = NeuralNetwork()

# Define the loss function
criterion = nn.CrossEntropyLoss()

# Define the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Sample input data
input_data = torch.randn(1, 10) # Reshaped to (1, 10)

# Perform forward pass
output = model(input_data)

# Perform backward pass and update the weights
optimizer.zero_grad()
loss = criterion(output, torch.tensor([1])) # Assuming the torget class is 1

# Print the updated model parameters
print('Updated model parameters: ')
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.data)

# Print the loss value
print('Loss:', loss.item())

# New function to calculate accuracy
def calculate_accuracy(output, target):
    _, predicted = torch.max(output, 1)
    accuracy = (predicted == target).sum().item() / target.size(0)
    return accuracy

# Calculate and print the accuracy
target = torch.tensor([1]) # Assuming the target class is 1
accuracy = calculate_accuracy(output, target)
print("Accuracy:", accuracy)