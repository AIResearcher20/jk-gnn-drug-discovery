import torch
import torch.nn as nn
from torch_geometric.nn import GINConv, global_mean_pool

class GIN(torch.nn.Module):
    def __init__(self, in_dim):
        super().__init__()

        def mlp():
            return nn.Sequential(
                nn.Linear(in_dim, 64),
                nn.ReLU(),
                nn.Linear(64, 64)
            )

        self.conv1 = GINConv(mlp())
        self.conv2 = GINConv(nn.Sequential(nn.Linear(64,64), nn.ReLU(), nn.Linear(64,64)))
        self.conv3 = GINConv(nn.Sequential(nn.Linear(64,64), nn.ReLU(), nn.Linear(64,64)))

        self.lin = nn.Linear(64, 1)

    def forward(self, x, edge_index, batch):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index).relu()
        x = self.conv3(x, edge_index).relu()

        x = global_mean_pool(x, batch)
        return self.lin(x)
