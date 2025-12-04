"""
Dead-zone time surface as a function of timing and ovality.
Uses chainring mean radius R directly (no tooth count).
"""

import os
import numpy as np
import plotly.graph_objects as go

from ovalchainring.pedalling_model import compute_pedal_force, compute_dead_zone_duration
from ovalchainring.chainring_oval import radius_oval

# Force model parameters (match the rest of the project)
H = 30.0
V = 150.0
N_EXP = 3

OUTPUT_DIR = "outputs"


def deadzone_grid(
    R: float,
    torque_threshold: float = 4.0,
    cadence_rpm: float = 90.0,
    ovalities_pct=None,
    timings_deg=None,
    n_points: int = 360,
):
    """
    Compute time spent below threshold (s per revolution) for a grid of (timing, ovality).
    Returns (T, O, Z) where Z has shape (len(ovalities), len(timings)).
    """
    ovalities_pct = (
        np.linspace(0.0, 20.0, 21) if ovalities_pct is None else np.asarray(ovalities_pct)
    )
    timings_deg = (
        np.linspace(0.0, 180.0, 181) if timings_deg is None else np.asarray(timings_deg)
    )

    angles = np.linspace(0, 2 * np.pi, n_points)
    forces = compute_pedal_force(angles, H=H, V=V, n=N_EXP)

    Z = np.zeros((len(ovalities_pct), len(timings_deg)))  # ovality x timing

    for i, ovality_pct in enumerate(ovalities_pct):
        ovality = ovality_pct / 100.0
        for j, timing_deg in enumerate(timings_deg):
            timing_rad = np.deg2rad(timing_deg)
            lever = radius_oval(angles, R=R, ovality=ovality, timing=timing_rad)
            torque = forces * lever
            dead_time, _, _ = compute_dead_zone_duration(
                angles, torque, torque_threshold, cadence_rpm=cadence_rpm
            )
            Z[i, j] = dead_time

    T, O = np.meshgrid(timings_deg, ovalities_pct)  # for plotting
    return T, O, Z


def deadzone_surface(
    R: float,
    torque_threshold: float = 4.0,
    cadence_rpm: float = 90.0,
    ovalities_pct=None,
    timings_deg=None,
    n_points: int = 360,
):
    """Return interactive Plotly surface figure."""
    T, O, Z = deadzone_grid(
        R=R,
        torque_threshold=torque_threshold,
        cadence_rpm=cadence_rpm,
        ovalities_pct=ovalities_pct,
        timings_deg=timings_deg,
        n_points=n_points,
    )

    fig = go.Figure(data=[go.Surface(z=Z, x=T, y=O, colorscale="Viridis")])
    fig.update_layout(
        title="Time below torque threshold vs timing & ovality",
        scene=dict(
            xaxis_title="Timing angle (°)",
            yaxis_title="Ovality (%)",
            zaxis_title="Time below threshold (s/rev)",
        ),
        width=900,
        height=800,
    )
    return fig