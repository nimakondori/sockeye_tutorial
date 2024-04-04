import os
from torch import nn, utils
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor


# setup data
dataset = MNIST(os.getcwd(), download=True, transform=ToTensor())
train_loader = utils.data.DataLoader(dataset, num_workers=4, 
                                     persistent_workers=True, 
                                     shuffle=True)