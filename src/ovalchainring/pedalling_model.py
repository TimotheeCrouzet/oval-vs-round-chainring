# src/ovalchainring/pedalling_model.py
import numpy as np
from ovalchainring.chainring_oval import radius_round, radius_oval


def compute_pedal_force(angle, H=30.0, V=150.0, n=3):
    """
    Pedal force model (independent of chainring shape):

    F(θ) = H · |cos^n(θ)| + V · |sin^n(θ)|

    with n = 3, H = 30 N, V = 150 N by default.
    """
    cos_term = np.abs(np.cos(angle)) ** n
    sin_term = np.abs(np.sin(angle)) ** n
    return H * cos_term + V * sin_term

def compute_crank_torque(angle,
                         chainring_radius,
                         H=30.0,
                         V=150.0,
                         n=3):
    """
    Compute torques at the crank based on rider force and chainring geometry.
    """
    F = compute_pedal_force(angle, H=H, V=V, n=n)
    return F * chainring_radius


def simulate_round(R=0.186, n=360):
    angle = np.linspace(0, 2*np.pi, n)
    chainring_radius = radius_round(R)
    torque = compute_crank_torque(angle, chainring_radius)
    return angle, torque, chainring_radius

def simulate_oval(R=0.186, ovality=0.12, timing=108, n=360):
    angle = np.linspace(0, 2*np.pi, n)
    chainring_radius = radius_oval(angle, R, ovality, timing)
    torque = compute_crank_torque(angle, chainring_radius)
    return angle, torque, chainring_radius

def compute_mean_torque(torque):
    return np.mean(torque)


def compute_dead_zone_duration(angle, torque, threshold, cadence_rpm=90):
    """
    Compute the total time spent in the dead zone:
    torque < threshold.

    angle : np.ndarray in radians (0 → 2π)
    torque : same length
    threshold : float (Nm)
    cadence_rpm : pedalling cadence (default 90 rpm)
    """
    mask = torque < threshold
    omega = 2 * np.pi * (cadence_rpm / 60.0)        # rad/s
    dt = np.diff(angle, append=angle[-1] + (angle[1] - angle[0])) / omega
    dead_time = np.sum(dt[mask])
    total_time = (2 * np.pi) / omega
    percent = 100 * dead_time / total_time
    return dead_time, total_time, percent

