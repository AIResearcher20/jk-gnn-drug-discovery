# GNN-based Blood-Brain Barrier Prediction

## Abstract
This study applies a Graph Neural Network (GIN) to predict Blood-Brain Barrier (BBB) permeability using molecular graph representations derived from SMILES strings.

---

## 1. Introduction
Predicting BBB permeability is a key task in CNS drug discovery. Experimental methods are costly, so computational models are widely used.

---

## 2. Methodology

2

### 2.1 Molecular Representation
- Molecules are represented as graphs
- Nodes: atoms
- Edges: chemical bonds

### 2.2 Model Architecture
- Graph Isomorphism Network (GIN)
- 3-layer message passing
- Global mean pooling
- Binary classification head

### 2.3 Training Setup
- Dataset: BBBP (2039 molecules)
- Loss: BCEWithLogitsLoss
- Optimizer: Adam

---

## 3. Results
- ROC-AUC: ~0.74
- PR-AUC: ~0.89
- MCC: ~0.44

---

## 4. Discussion
The model successfully learns molecular structural patterns but remains a baseline approach without advanced optimization or scaffold splitting.

---

## 5. Conclusion
This work demonstrates a reproducible pipeline for molecular property prediction using Graph Neural Networks.

---

## 6. Keywords
Graph Neural Networks, BBBP, SMILES, Molecular Graphs, Virtual Screening
