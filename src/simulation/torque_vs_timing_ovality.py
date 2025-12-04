"""
Mean torque surface as a function of timing and ovality.
Uses chainring mean radius R directly.
"""

import os
import numpy as np
import plotly.graph_objects as go

from ovalchainring.pedalling_model import compute_pedal_force
from ovalchainring.chainring_oval import radius_oval

# Force model parameters 
H = 30.0
V = 150.0
N_EXP = 3

OUTPUT_DIR = "outputs"


def mean_torque_grid(
    R: float,
    ovalities_pct=None,
    timings_deg=None,
    n_points: int = 360,
):
    """Compute mean torque for a grid of (timing, ovality) given mean radius R."""
    ovalities_pct = (
        np.linspace(0.0, 20.0, 21) if ovalities_pct is None else np.asarray(ovalities_pct)
    )
    timings_deg = (
        np.linspace(0.0, 180.0, 181) if timings_deg is None else np.asarray(timings_deg)
    )

    angles = np.linspace(0, 2 * np.pi, n_points)
    forces = compute_pedal_force(angles, H=H, V=V, n=N_EXP)

    mean_torque = np.zeros((len(ovalities_pct), len(timings_deg)))

    for i, ovality_pct in enumerate(ovalities_pct):
        ovality = ovality_pct / 100.0
        for j, timing_deg in enumerate(timings_deg):
            timing_rad = np.deg2rad(timing_deg)
            lever_eff = radius_oval(angles, R=R, ovality=ovality, timing=timing_rad)
            torque = lever_eff * forces
            mean_torque[i, j] = torque.mean()

    T, O = np.meshgrid(timings_deg, ovalities_pct)  # pour le plot
    return T, O, mean_torque


def mean_torque_surface(
    R: float,
    ovalities_pct=None,
    timings_deg=None,
    n_points: int = 360,
):
    """Return interactive Plotly surface figure."""
    T, O, Z = mean_torque_grid(
        R=R,
        ovalities_pct=ovalities_pct,
        timings_deg=timings_deg,
        n_points=n_points,
    )

    fig = go.Figure(data=[go.Surface(z=Z, x=T, y=O, colorscale="Viridis")])
    fig.update_layout(
        title="Mean torque vs timing & ovality",
        scene=dict(
            xaxis_title="Timing angle (°)",
            yaxis_title="Ovality (%)",
            zaxis_title="Mean torque (N·m)",
        ),
        width=900,
        height=800,
    )
    return fig

