import torch
from torch_geometric.datasets import MoleculeNet
from torch_geometric.loader import DataLoader
from model import GIN
import torch.nn.functional as F

dataset = MoleculeNet(root="data", name="BBBP")

train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = GIN(dataset.num_features).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.BCEWithLogitsLoss()

for epoch in range(20):
    model.train()
    total_loss = 0

    for batch in train_loader:
        batch = batch.to(device)

        optimizer.zero_grad()
        out = model(batch.x.float(), batch.edge_index, batch.batch).view(-1)

        loss = loss_fn(out, batch.y.view(-1).float())
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print("Epoch:", epoch, "Loss:", total_loss)
