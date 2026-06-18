from dataclasses import dataclass

@dataclass
class Config:

    seed: int = 42

    batch_size: int = 64
    lr: float = 1e-3
    epochs: int = 30

    hidden_dim: int = 128
    n_folds: int = 5
