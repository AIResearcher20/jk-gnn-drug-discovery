import torch
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score
from torch_geometric.datasets import MoleculeNet
from torch_geometric.loader import DataLoader
from model import GIN

dataset = MoleculeNet(root="data", name="BBBP")
loader = DataLoader(dataset, batch_size=32)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = GIN(dataset.num_features).to(device)
model.load_state_dict(torch.load("models/gin_bbbp.pt"))
model.eval()

y_true, y_prob = [], []

for batch in loader:
    batch = batch.to(device)

    with torch.no_grad():
        out = model(batch.x.float(), batch.edge_index, batch.batch).view(-1)
        prob = torch.sigmoid(out)

    y_true.extend(batch.y.cpu().numpy().reshape(-1))
    y_prob.extend(prob.cpu().numpy().reshape(-1))

print("AUC:", roc_auc_score(y_true, y_prob))
print("PR-AUC:", average_precision_score(y_true, y_prob))
