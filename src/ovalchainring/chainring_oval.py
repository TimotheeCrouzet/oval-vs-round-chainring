# src/ovalchainring/chainring_oval.py
import numpy as np

def radius_round(R):
    """Return constant radius (round chainring)."""
    return R

def radius_oval(angle, R, ovality, timing):
    """
    Compute radius of an oval chainring as a function of angle.
    angle : rad
    R : base radius
    ovality : e.g. 0.1 for 10%
    timing : rad (rotation of ellipse major axis)
    """
    # Exemple tiré de ton script :
    return R * (1 + ovality * np.cos(2 * (angle - timing)))
