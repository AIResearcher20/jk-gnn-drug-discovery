from torch_geometric.datasets import MoleculeNet

def load_data():
    dataset = MoleculeNet(root="data", name="BBBP")
    return dataset
