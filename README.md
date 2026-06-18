readme1"
# GNN-based Blood-Brain Barrier Prediction

## 🧪 Overview
This project implements a Graph Neural Network (GIN) for predicting Blood-Brain Barrier (BBB) permeability using molecular graph representations.

## 🧠 Method
- Graph Neural Networks (GIN)
- Molecular graph representation from SMILES
- Global mean pooling for graph-level prediction

## 📊 Dataset
BBBP dataset from MoleculeNet (2039 molecules)

## 📈 Results
- ROC-AUC: ~0.74
- PR-AUC: ~0.89

## 🔬 Application
Virtual screening for drug discovery and CNS drug design.

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/train.py
📦 Output
trained model
prediction scores
ranked molecular candidates
Copy code

---

# 📦 3. requirements.txt

```text id="req1"
torch
torch-geometric
scikit-learn
pandas
numpy
matplotlib
rdkit
