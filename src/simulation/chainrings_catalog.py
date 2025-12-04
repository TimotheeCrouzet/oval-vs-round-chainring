# src/simulation/chainrings_catalog.py

from dataclasses import dataclass
import numpy as np

@dataclass
class ChainringConfig:
    name: str
    R: float          # rayon moyen (m)
    ovality: float    # 0.0 = rond, 0.12 = 12%
    timing_deg: float # timing en degrés

    @property
    def timing_rad(self) -> float:
        return np.deg2rad(self.timing_deg)

CHAINRINGS = [
    ChainringConfig(
        name="Round 42T (référence)",
        R=0.1,
        ovality=0.0,
        timing_deg=0.0,
    ),
    ChainringConfig(
        name="Oval 42T - 12% - 108°",
        R=0.1,
        ovality=0.12,
        timing_deg=108.0,
    ),
    ChainringConfig(
        name="Oval 50T - 10% - 110°",
        R=0.12,
        ovality=0.10,
        timing_deg=110.0,
    ),
    # etc pour tes vrais plateaux du marché
]
